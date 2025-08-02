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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
hpnicfQinQv2=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,137))
if mibBuilder.loadTexts:hpnicfQinQv2.setRevisions(('2013-03-08 00:00',))
_HpnicfQinQv2MibObject_ObjectIdentity=ObjectIdentity
hpnicfQinQv2MibObject=_HpnicfQinQv2MibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,137,1))
_HpnicfQinQv2ScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfQinQv2ScalarObjects=_HpnicfQinQv2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,137,1,1))
class _HpnicfQinQv2ServiceTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQv2ServiceTPID_Type.__name__=_C
_HpnicfQinQv2ServiceTPID_Object=MibScalar
hpnicfQinQv2ServiceTPID=_HpnicfQinQv2ServiceTPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,1,1),_HpnicfQinQv2ServiceTPID_Type())
hpnicfQinQv2ServiceTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQv2ServiceTPID.setStatus(_A)
class _HpnicfQinQv2CustomerTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQv2CustomerTPID_Type.__name__=_C
_HpnicfQinQv2CustomerTPID_Object=MibScalar
hpnicfQinQv2CustomerTPID=_HpnicfQinQv2CustomerTPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,1,2),_HpnicfQinQv2CustomerTPID_Type())
hpnicfQinQv2CustomerTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQv2CustomerTPID.setStatus(_A)
_HpnicfQinQv2IfCfgTable_Object=MibTable
hpnicfQinQv2IfCfgTable=_HpnicfQinQv2IfCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,2))
if mibBuilder.loadTexts:hpnicfQinQv2IfCfgTable.setStatus(_A)
_HpnicfQinQv2IfCfgEntry_Object=MibTableRow
hpnicfQinQv2IfCfgEntry=_HpnicfQinQv2IfCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,2,1))
hpnicfQinQv2IfCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfQinQv2IfCfgEntry.setStatus(_A)
class _HpnicfQinQv2IfState_Type(TruthValue):defaultValue=2
_HpnicfQinQv2IfState_Type.__name__=_G
_HpnicfQinQv2IfState_Object=MibTableColumn
hpnicfQinQv2IfState=_HpnicfQinQv2IfState_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,2,1,1),_HpnicfQinQv2IfState_Type())
hpnicfQinQv2IfState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQv2IfState.setStatus(_A)
class _HpnicfQinQv2IfServiceTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQv2IfServiceTPID_Type.__name__=_C
_HpnicfQinQv2IfServiceTPID_Object=MibTableColumn
hpnicfQinQv2IfServiceTPID=_HpnicfQinQv2IfServiceTPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,2,1,2),_HpnicfQinQv2IfServiceTPID_Type())
hpnicfQinQv2IfServiceTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQv2IfServiceTPID.setStatus(_A)
class _HpnicfQinQv2IfCustomerTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQv2IfCustomerTPID_Type.__name__=_C
_HpnicfQinQv2IfCustomerTPID_Object=MibTableColumn
hpnicfQinQv2IfCustomerTPID=_HpnicfQinQv2IfCustomerTPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,2,1,3),_HpnicfQinQv2IfCustomerTPID_Type())
hpnicfQinQv2IfCustomerTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQv2IfCustomerTPID.setStatus(_A)
class _HpnicfQinQv2IfTransVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_HpnicfQinQv2IfTransVlanList_Type.__name__=_D
_HpnicfQinQv2IfTransVlanList_Object=MibTableColumn
hpnicfQinQv2IfTransVlanList=_HpnicfQinQv2IfTransVlanList_Object((1,3,6,1,4,1,11,2,14,11,15,2,137,1,2,1,4),_HpnicfQinQv2IfTransVlanList_Type())
hpnicfQinQv2IfTransVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQv2IfTransVlanList.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-QINQV2-MIB',**{'hpnicfQinQv2':hpnicfQinQv2,'hpnicfQinQv2MibObject':hpnicfQinQv2MibObject,'hpnicfQinQv2ScalarObjects':hpnicfQinQv2ScalarObjects,'hpnicfQinQv2ServiceTPID':hpnicfQinQv2ServiceTPID,'hpnicfQinQv2CustomerTPID':hpnicfQinQv2CustomerTPID,'hpnicfQinQv2IfCfgTable':hpnicfQinQv2IfCfgTable,'hpnicfQinQv2IfCfgEntry':hpnicfQinQv2IfCfgEntry,'hpnicfQinQv2IfState':hpnicfQinQv2IfState,'hpnicfQinQv2IfServiceTPID':hpnicfQinQv2IfServiceTPID,'hpnicfQinQv2IfCustomerTPID':hpnicfQinQv2IfCustomerTPID,'hpnicfQinQv2IfTransVlanList':hpnicfQinQv2IfTransVlanList})