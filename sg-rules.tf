module sg_first_sg_rule1 {
  source = "./sg-rules"
  create_sg  = var.create_sg
  sg_name = "first_sg"
  type = "ingress"
  rule_list = ["22-22-tcp"]
  ref_sg_name = "second_sg"
  sg_name_id = module.sg.sg_name_id
}

module sg_second_sg_rule1 {
  source = "./sg-rules"
  create_sg  = var.create_sg
  sg_name = "second_sg"
  type = "ingress"
  rule_list = ["22-22-tcp"]
  ref_sg_name = "first-sg"
  sg_name_id = module.sg.sg_name_id
}

