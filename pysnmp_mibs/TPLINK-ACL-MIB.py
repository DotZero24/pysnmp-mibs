_K='tpAclBindVlan'
_J='tpAclVlanBindAclId'
_I='tpAclPortBindAclId'
_H='default'
_G='tpAclActionRuleId'
_F='tpAclActionAclId'
_E='read-only'
_D='Integer32'
_C='TPLINK-ACL-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkAclMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,26))
if mibBuilder.loadTexts:tplinkAclMIB.setRevisions(('2012-12-13 09:30',))
_TplinkAclMIBObjects_ObjectIdentity=ObjectIdentity
tplinkAclMIBObjects=_TplinkAclMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1))
_TpAclActionConfigure_ObjectIdentity=ObjectIdentity
tpAclActionConfigure=_TpAclActionConfigure_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1,3))
_TpAclActionTable_Object=MibTable
tpAclActionTable=_TpAclActionTable_Object((1,3,6,1,4,1,11863,6,26,1,3,1))
if mibBuilder.loadTexts:tpAclActionTable.setStatus(_A)
_TpAclActionEntry_Object=MibTableRow
tpAclActionEntry=_TpAclActionEntry_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1))
tpAclActionEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:tpAclActionEntry.setStatus(_A)
_TpAclActionAclId_Type=Integer32
_TpAclActionAclId_Object=MibTableColumn
tpAclActionAclId=_TpAclActionAclId_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,1),_TpAclActionAclId_Type())
tpAclActionAclId.setMaxAccess(_E)
if mibBuilder.loadTexts:tpAclActionAclId.setStatus(_A)
_TpAclActionRuleId_Type=Integer32
_TpAclActionRuleId_Object=MibTableColumn
tpAclActionRuleId=_TpAclActionRuleId_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,2),_TpAclActionRuleId_Type())
tpAclActionRuleId.setMaxAccess(_E)
if mibBuilder.loadTexts:tpAclActionRuleId.setStatus(_A)
_TpAclActionMirrorPort_Type=OctetString
_TpAclActionMirrorPort_Object=MibTableColumn
tpAclActionMirrorPort=_TpAclActionMirrorPort_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,3),_TpAclActionMirrorPort_Type())
tpAclActionMirrorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionMirrorPort.setStatus(_A)
_TpAclActionRedirectPort_Type=OctetString
_TpAclActionRedirectPort_Object=MibTableColumn
tpAclActionRedirectPort=_TpAclActionRedirectPort_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,4),_TpAclActionRedirectPort_Type())
tpAclActionRedirectPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionRedirectPort.setStatus(_A)
_TpAclActionConditionRate_Type=Integer32
_TpAclActionConditionRate_Object=MibTableColumn
tpAclActionConditionRate=_TpAclActionConditionRate_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,5),_TpAclActionConditionRate_Type())
tpAclActionConditionRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionConditionRate.setStatus(_A)
_TpAclActionConditionBurst_Type=Integer32
_TpAclActionConditionBurst_Object=MibTableColumn
tpAclActionConditionBurst=_TpAclActionConditionBurst_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,6),_TpAclActionConditionBurst_Type())
tpAclActionConditionBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionConditionBurst.setStatus(_A)
class _TpAclActionConditionExceedOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('discard',1),('remark-DSCP',2)))
_TpAclActionConditionExceedOperation_Type.__name__=_D
_TpAclActionConditionExceedOperation_Object=MibTableColumn
tpAclActionConditionExceedOperation=_TpAclActionConditionExceedOperation_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,7),_TpAclActionConditionExceedOperation_Type())
tpAclActionConditionExceedOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionConditionExceedOperation.setStatus(_A)
_TpAclActionConditionRemarkDscp_Type=Integer32
_TpAclActionConditionRemarkDscp_Object=MibTableColumn
tpAclActionConditionRemarkDscp=_TpAclActionConditionRemarkDscp_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,8),_TpAclActionConditionRemarkDscp_Type())
tpAclActionConditionRemarkDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionConditionRemarkDscp.setStatus(_A)
class _TpAclActionQosRemarkDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64)));namedValues=NamedValues(*(('dscp0-be-000000',0),('dscp1',1),('dscp2',2),('dscp3',3),('dscp4',4),('dscp5',5),('dscp6',6),('dscp7',7),('dscp8-cs1-001000',8),('dscp9',9),('dscp10-af11-001010',10),('dscp11',11),('dscp12-af12-001100',12),('dscp13',13),('dscp14-af13-001110',14),('dscp15',15),('dscp16-cs2-010000',16),('dscp17',17),('dscp18-af21-010010',18),('dscp19',19),('dscp20-af22-010100',20),('dscp21',21),('dscp22-af23-010110',22),('dscp23',23),('dscp24-cs3-011000',24),('dscp25',25),('dscp26-af31-011010',26),('dscp27',27),('dscp28-af32-011100',28),('dscp29',29),('dscp30-af33-011110',30),('dscp31',31),('dscp32-cs4-100000',32),('dscp33',33),('dscp34-af41-100010',34),('dscp35',35),('dscp36-af42-100100',36),('dscp37',37),('dscp38-af43-100110',38),('dscp39',39),('dscp40-cs5-101000',40),('dscp41',41),('dscp42',42),('dscp43',43),('dscp44',44),('dscp45',45),('dscp46-ef-101110',46),('dscp47',47),('dscp48-cs6-110000',48),('dscp49',49),('dscp50',50),('dscp51',51),('dscp52',52),('dscp53',53),('dscp54',54),('dscp55',55),('dscp56-cs7-111000',56),('dscp57',57),('dscp58',58),('dscp59',59),('dscp60',60),('dscp61',61),('dscp62',62),('dscp63',63),('dscp64-noLimit',64)))
_TpAclActionQosRemarkDscp_Type.__name__=_D
_TpAclActionQosRemarkDscp_Object=MibTableColumn
tpAclActionQosRemarkDscp=_TpAclActionQosRemarkDscp_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,9),_TpAclActionQosRemarkDscp_Type())
tpAclActionQosRemarkDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionQosRemarkDscp.setStatus(_A)
class _TpAclActionQosRemarkLocalPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('tc0',0),('tc1',1),('tc2',2),('tc3',3),('tc4',4),('tc5',5),('tc6',6),('tc7',7),(_H,8)))
_TpAclActionQosRemarkLocalPri_Type.__name__=_D
_TpAclActionQosRemarkLocalPri_Object=MibTableColumn
tpAclActionQosRemarkLocalPri=_TpAclActionQosRemarkLocalPri_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,10),_TpAclActionQosRemarkLocalPri_Type())
tpAclActionQosRemarkLocalPri.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionQosRemarkLocalPri.setStatus(_A)
class _TpAclActionQosRemark8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cos0',0),('cos1',1),('cos2',2),('cos3',3),('cos4',4),('cos5',5),('cos6',6),('cos7',7),(_H,8)))
_TpAclActionQosRemark8021p_Type.__name__=_D
_TpAclActionQosRemark8021p_Object=MibTableColumn
tpAclActionQosRemark8021p=_TpAclActionQosRemark8021p_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,11),_TpAclActionQosRemark8021p_Type())
tpAclActionQosRemark8021p.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionQosRemark8021p.setStatus(_A)
_TpAclActionStatus_Type=TPRowStatus
_TpAclActionStatus_Object=MibTableColumn
tpAclActionStatus=_TpAclActionStatus_Object((1,3,6,1,4,1,11863,6,26,1,3,1,1,12),_TpAclActionStatus_Type())
tpAclActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclActionStatus.setStatus(_A)
_TpAclPortBindConfigure_ObjectIdentity=ObjectIdentity
tpAclPortBindConfigure=_TpAclPortBindConfigure_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1,4))
_TpAclPortBindTable_Object=MibTable
tpAclPortBindTable=_TpAclPortBindTable_Object((1,3,6,1,4,1,11863,6,26,1,4,1))
if mibBuilder.loadTexts:tpAclPortBindTable.setStatus(_A)
_TpAclPortBindEntry_Object=MibTableRow
tpAclPortBindEntry=_TpAclPortBindEntry_Object((1,3,6,1,4,1,11863,6,26,1,4,1,1))
tpAclPortBindEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:tpAclPortBindEntry.setStatus(_A)
_TpAclPortBindAclId_Type=Integer32
_TpAclPortBindAclId_Object=MibTableColumn
tpAclPortBindAclId=_TpAclPortBindAclId_Object((1,3,6,1,4,1,11863,6,26,1,4,1,1,1),_TpAclPortBindAclId_Type())
tpAclPortBindAclId.setMaxAccess(_E)
if mibBuilder.loadTexts:tpAclPortBindAclId.setStatus(_A)
_TpAclBindPortList_Type=OctetString
_TpAclBindPortList_Object=MibTableColumn
tpAclBindPortList=_TpAclBindPortList_Object((1,3,6,1,4,1,11863,6,26,1,4,1,1,2),_TpAclBindPortList_Type())
tpAclBindPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclBindPortList.setStatus(_A)
_TpAclPortBindStatus_Type=TPRowStatus
_TpAclPortBindStatus_Object=MibTableColumn
tpAclPortBindStatus=_TpAclPortBindStatus_Object((1,3,6,1,4,1,11863,6,26,1,4,1,1,3),_TpAclPortBindStatus_Type())
tpAclPortBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclPortBindStatus.setStatus(_A)
_TpAclVlanBindConfigure_ObjectIdentity=ObjectIdentity
tpAclVlanBindConfigure=_TpAclVlanBindConfigure_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1,5))
_TpAclVlanBindTable_Object=MibTable
tpAclVlanBindTable=_TpAclVlanBindTable_Object((1,3,6,1,4,1,11863,6,26,1,5,2))
if mibBuilder.loadTexts:tpAclVlanBindTable.setStatus(_A)
_TpAclVlanBindEntry_Object=MibTableRow
tpAclVlanBindEntry=_TpAclVlanBindEntry_Object((1,3,6,1,4,1,11863,6,26,1,5,2,1))
tpAclVlanBindEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:tpAclVlanBindEntry.setStatus(_A)
_TpAclVlanBindAclId_Type=Integer32
_TpAclVlanBindAclId_Object=MibTableColumn
tpAclVlanBindAclId=_TpAclVlanBindAclId_Object((1,3,6,1,4,1,11863,6,26,1,5,2,1,1),_TpAclVlanBindAclId_Type())
tpAclVlanBindAclId.setMaxAccess(_E)
if mibBuilder.loadTexts:tpAclVlanBindAclId.setStatus(_A)
_TpAclBindVlan_Type=Integer32
_TpAclBindVlan_Object=MibTableColumn
tpAclBindVlan=_TpAclBindVlan_Object((1,3,6,1,4,1,11863,6,26,1,5,2,1,2),_TpAclBindVlan_Type())
tpAclBindVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:tpAclBindVlan.setStatus(_A)
_TpAclVlanBindStatus_Type=TPRowStatus
_TpAclVlanBindStatus_Object=MibTableColumn
tpAclVlanBindStatus=_TpAclVlanBindStatus_Object((1,3,6,1,4,1,11863,6,26,1,5,2,1,3),_TpAclVlanBindStatus_Type())
tpAclVlanBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpAclVlanBindStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'tplinkAclMIB':tplinkAclMIB,'tplinkAclMIBObjects':tplinkAclMIBObjects,'tpAclActionConfigure':tpAclActionConfigure,'tpAclActionTable':tpAclActionTable,'tpAclActionEntry':tpAclActionEntry,_F:tpAclActionAclId,_G:tpAclActionRuleId,'tpAclActionMirrorPort':tpAclActionMirrorPort,'tpAclActionRedirectPort':tpAclActionRedirectPort,'tpAclActionConditionRate':tpAclActionConditionRate,'tpAclActionConditionBurst':tpAclActionConditionBurst,'tpAclActionConditionExceedOperation':tpAclActionConditionExceedOperation,'tpAclActionConditionRemarkDscp':tpAclActionConditionRemarkDscp,'tpAclActionQosRemarkDscp':tpAclActionQosRemarkDscp,'tpAclActionQosRemarkLocalPri':tpAclActionQosRemarkLocalPri,'tpAclActionQosRemark8021p':tpAclActionQosRemark8021p,'tpAclActionStatus':tpAclActionStatus,'tpAclPortBindConfigure':tpAclPortBindConfigure,'tpAclPortBindTable':tpAclPortBindTable,'tpAclPortBindEntry':tpAclPortBindEntry,_I:tpAclPortBindAclId,'tpAclBindPortList':tpAclBindPortList,'tpAclPortBindStatus':tpAclPortBindStatus,'tpAclVlanBindConfigure':tpAclVlanBindConfigure,'tpAclVlanBindTable':tpAclVlanBindTable,'tpAclVlanBindEntry':tpAclVlanBindEntry,_J:tpAclVlanBindAclId,_K:tpAclBindVlan,'tpAclVlanBindStatus':tpAclVlanBindStatus})