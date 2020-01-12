variable sg_list {default = []}
sg_list   = [
{
 name = "first_sg"
 desc = "First security Group"
 traffic_rules = [
   {
     rule_list = ["22-22-tcp"]
     type = "ingress"
     ref_sg_name = "second_sg"
   }
 ]
},
{
 name = "second_sg"
 desc = "Second security Group"
 traffic_rules = [
   {
     rule_list = ["22-22-tcp"]
     type = "ingress"
     ref_sg_name = "first-sg"
   }
 ]
}]
