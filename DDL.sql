create table o_fruit_list_d(
id int(11) not null auto_increment comment '自增id',
fruit varchar(20) comment '果蔬名称',
fruit_class varchar(10) comment '果蔬种类(水果/蔬菜)',
into_price double comment '进货单价/kg',
sale_price double comment '建议零售价/kg',
fruit_weight float comment '重量',
create_time datetime comment '创建时间',
update_time datetime comment '更新时间',
PRIMARY KEY (`ID`),
 KEY `IDX_fruit` (`fruit`)
)comment '果蔬明细表';


insert into o_fruit_list_d(fruit,fruit_class,into_price,sale_price,fruit_weight,create_time,update_time) values('苹果','水果',1.05,3.0,100,'2019-09-05','2019-09-05');
insert into o_fruit_list_d(fruit,fruit_class,into_price,sale_price,fruit_weight,create_time,update_time) values('香蕉','水果',1.5,4.0,100,'2019-09-05','2019-09-05');
insert into o_fruit_list_d(fruit,fruit_class,into_price,sale_price,fruit_weight,create_time,update_time) values('西红柿','蔬菜',0.5,1.5,100,'2019-09-05','2019-09-05');


