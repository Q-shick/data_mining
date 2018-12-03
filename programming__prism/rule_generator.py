import pprint

def rule_evaluator(df, class_val, attr_list):
    """ calculate accuracy by attribute
    ex) {"attribute 1": (attribute value, class coverage, candidate coverage, accuracy)...} """
    rule_candidates = {}

    for attr in attr_list: # iterate attributes
        rule_candidates[attr] = []
        for val in df[attr].unique():
            candidate = df.loc[df[attr]==val]
            num_candidate = len(candidate)
            class_cnt = len(candidate[candidate['class']==class_val]) # obs of the class
            accu = float(class_cnt)/num_candidate
            rule_candidates[attr].append( (val, class_cnt, num_candidate, round(accu, 3)) )

    pprint.pprint(rule_candidates)

    return rule_candidates


def rule_selector(rule_dict):
    """ refine a rule by comparing accuracy and return the attribute and its value
    ex) "age" = "young" """
    max_attr = "NA"
    max_attr_val = "NA"
    max_coverage = 0
    max_attr_num = 0
    max_accu = 0

    for key, val in rule_dict.items(): # comparison
        for candidate in val:
            if (candidate[3] > max_accu) or (candidate[3] == max_accu and candidate[2] > max_attr_num):
                max_attr, max_attr_val, max_coverage, max_attr_num, max_accu = \
                        key, candidate[0], candidate[1], candidate[2], candidate[3]

    print("<Selected Attribute: " + max_attr + " = " + str(max_attr_val) + '>\n')

    return max_attr, max_attr_val, max_attr_num, max_accu


def rule_finder(df, class_val, attr_list, rule_set):
    """ find a rule by calling rule_evaluator and rule_selector
    the function works recursively until it finds """
    if len(attr_list) == 0: # used all attributes
        return rule_set

    # find a better accuracy if some attributes are left
    rule_candidates = rule_evaluator(df, class_val, attr_list)
    rule_attr, rule_val, rule_coverage, rule_accuracy = rule_selector(rule_candidates)
    rule_set.append( (rule_attr, rule_val) )

    if rule_accuracy == 1.0: # perfect accuracy
        return rule_set

    # remove the attribute if not perfect
    df = df[df[rule_attr]==rule_val]
    attr_list.remove(rule_attr)
    rule_finder(df, class_val, attr_list, rule_set)

    return rule_set # finally found rule


def remove_instances(df, class_val, rule):
    """ remove from a data frame the instances a rule covers """
    temp_df = df
    for r in rule: # rule_tuple = (attribute, value)
        attr, val = r[0], r[1]
        temp_df = temp_df[temp_df[attr]==val]

    inst_idx = temp_df.index
    num_class = len(temp_df[temp_df['class']==class_val])
    df = df.loc[set(df.index) - set(inst_idx)] # removal
    overall_accu = float(num_class)/len(inst_idx) if len(inst_idx) != 0 else 0

    return df, round(overall_accu, 3)
