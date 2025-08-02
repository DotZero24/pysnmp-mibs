_G='TruthValue'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
h3cQinQv2=ModuleIdentity((1,3,6,1,4,1,2011,10,2,137))
if mibBuilder.loadTexts:h3cQinQv2.setRevisions(('2013-03-08 00:00',))
_H3cQinQv2MibObject_ObjectIdentity=ObjectIdentity
h3cQinQv2MibObject=_H3cQinQv2MibObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,137,1))
_H3cQinQv2ScalarObjects_ObjectIdentity=ObjectIdentity
h3cQinQv2ScalarObjects=_H3cQinQv2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,137,1,1))
class _H3cQinQv2ServiceTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQv2ServiceTPID_Type.__name__=_C
_H3cQinQv2ServiceTPID_Object=MibScalar
h3cQinQv2ServiceTPID=_H3cQinQv2ServiceTPID_Object((1,3,6,1,4,1,2011,10,2,137,1,1,1),_H3cQinQv2ServiceTPID_Type())
h3cQinQv2ServiceTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQv2ServiceTPID.setStatus(_A)
class _H3cQinQv2CustomerTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQv2CustomerTPID_Type.__name__=_C
_H3cQinQv2CustomerTPID_Object=MibScalar
h3cQinQv2CustomerTPID=_H3cQinQv2CustomerTPID_Object((1,3,6,1,4,1,2011,10,2,137,1,1,2),_H3cQinQv2CustomerTPID_Type())
h3cQinQv2CustomerTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQv2CustomerTPID.setStatus(_A)
_H3cQinQv2IfCfgTable_Object=MibTable
h3cQinQv2IfCfgTable=_H3cQinQv2IfCfgTable_Object((1,3,6,1,4,1,2011,10,2,137,1,2))
if mibBuilder.loadTexts:h3cQinQv2IfCfgTable.setStatus(_A)
_H3cQinQv2IfCfgEntry_Object=MibTableRow
h3cQinQv2IfCfgEntry=_H3cQinQv2IfCfgEntry_Object((1,3,6,1,4,1,2011,10,2,137,1,2,1))
h3cQinQv2IfCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cQinQv2IfCfgEntry.setStatus(_A)
class _H3cQinQv2IfState_Type(TruthValue):defaultValue=2
_H3cQinQv2IfState_Type.__name__=_G
_H3cQinQv2IfState_Object=MibTableColumn
h3cQinQv2IfState=_H3cQinQv2IfState_Object((1,3,6,1,4,1,2011,10,2,137,1,2,1,1),_H3cQinQv2IfState_Type())
h3cQinQv2IfState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQv2IfState.setStatus(_A)
class _H3cQinQv2IfServiceTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQv2IfServiceTPID_Type.__name__=_C
_H3cQinQv2IfServiceTPID_Object=MibTableColumn
h3cQinQv2IfServiceTPID=_H3cQinQv2IfServiceTPID_Object((1,3,6,1,4,1,2011,10,2,137,1,2,1,2),_H3cQinQv2IfServiceTPID_Type())
h3cQinQv2IfServiceTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQv2IfServiceTPID.setStatus(_A)
class _H3cQinQv2IfCustomerTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQv2IfCustomerTPID_Type.__name__=_C
_H3cQinQv2IfCustomerTPID_Object=MibTableColumn
h3cQinQv2IfCustomerTPID=_H3cQinQv2IfCustomerTPID_Object((1,3,6,1,4,1,2011,10,2,137,1,2,1,3),_H3cQinQv2IfCustomerTPID_Type())
h3cQinQv2IfCustomerTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQv2IfCustomerTPID.setStatus(_A)
class _H3cQinQv2IfTransVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_H3cQinQv2IfTransVlanList_Type.__name__=_D
_H3cQinQv2IfTransVlanList_Object=MibTableColumn
h3cQinQv2IfTransVlanList=_H3cQinQv2IfTransVlanList_Object((1,3,6,1,4,1,2011,10,2,137,1,2,1,4),_H3cQinQv2IfTransVlanList_Type())
h3cQinQv2IfTransVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQv2IfTransVlanList.setStatus(_A)
mibBuilder.exportSymbols('H3C-QINQV2-MIB',**{'h3cQinQv2':h3cQinQv2,'h3cQinQv2MibObject':h3cQinQv2MibObject,'h3cQinQv2ScalarObjects':h3cQinQv2ScalarObjects,'h3cQinQv2ServiceTPID':h3cQinQv2ServiceTPID,'h3cQinQv2CustomerTPID':h3cQinQv2CustomerTPID,'h3cQinQv2IfCfgTable':h3cQinQv2IfCfgTable,'h3cQinQv2IfCfgEntry':h3cQinQv2IfCfgEntry,'h3cQinQv2IfState':h3cQinQv2IfState,'h3cQinQv2IfServiceTPID':h3cQinQv2IfServiceTPID,'h3cQinQv2IfCustomerTPID':h3cQinQv2IfCustomerTPID,'h3cQinQv2IfTransVlanList':h3cQinQv2IfTransVlanList})