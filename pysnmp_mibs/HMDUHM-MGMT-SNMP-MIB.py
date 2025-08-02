_R='hmDuHmRedCheckState'
_Q='hmDuHmRedIfOpState'
_P='hmDuHmRedIfIndex'
_O='hmDuHmRedGroupID'
_N='hmDuHmPrimIfOpState'
_M='absent'
_L='inactive-by-mgmt'
_K='active-by-mgmt'
_J='not-available'
_I='inactive'
_H='active'
_G='hmDuHmPrimIfIndex'
_F='hmDuHmPrimGroupID'
_E='read-write'
_D='read-only'
_C='HMDUHM-MGMT-SNMP-MIB'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmConfiguration,=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_HmDualHoming_ObjectIdentity=ObjectIdentity
hmDualHoming=_HmDualHoming_ObjectIdentity((1,3,6,1,4,1,248,14,4))
_HmDualHomingTable_Object=MibTable
hmDualHomingTable=_HmDualHomingTable_Object((1,3,6,1,4,1,248,14,4,1))
if mibBuilder.loadTexts:hmDualHomingTable.setStatus(_A)
_HmDuHmEntry_Object=MibTableRow
hmDuHmEntry=_HmDuHmEntry_Object((1,3,6,1,4,1,248,14,4,1,1))
hmDuHmEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:hmDuHmEntry.setStatus(_A)
class _HmDuHmPrimGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_HmDuHmPrimGroupID_Type.__name__=_B
_HmDuHmPrimGroupID_Object=MibTableColumn
hmDuHmPrimGroupID=_HmDuHmPrimGroupID_Object((1,3,6,1,4,1,248,14,4,1,1,1),_HmDuHmPrimGroupID_Type())
hmDuHmPrimGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDuHmPrimGroupID.setStatus(_A)
class _HmDuHmPrimIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmDuHmPrimIfIndex_Type.__name__=_B
_HmDuHmPrimIfIndex_Object=MibTableColumn
hmDuHmPrimIfIndex=_HmDuHmPrimIfIndex_Object((1,3,6,1,4,1,248,14,4,1,1,2),_HmDuHmPrimIfIndex_Type())
hmDuHmPrimIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDuHmPrimIfIndex.setStatus(_A)
class _HmDuHmPrimIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_H,2),(_K,3),(_L,4),(_I,5),(_M,6)))
_HmDuHmPrimIfOpState_Type.__name__=_B
_HmDuHmPrimIfOpState_Object=MibTableColumn
hmDuHmPrimIfOpState=_HmDuHmPrimIfOpState_Object((1,3,6,1,4,1,248,14,4,1,1,3),_HmDuHmPrimIfOpState_Type())
hmDuHmPrimIfOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDuHmPrimIfOpState.setStatus(_A)
_HmDuHmRedGroupID_Type=Integer32
_HmDuHmRedGroupID_Object=MibTableColumn
hmDuHmRedGroupID=_HmDuHmRedGroupID_Object((1,3,6,1,4,1,248,14,4,1,1,4),_HmDuHmRedGroupID_Type())
hmDuHmRedGroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmDuHmRedGroupID.setStatus(_A)
_HmDuHmRedIfIndex_Type=Integer32
_HmDuHmRedIfIndex_Object=MibTableColumn
hmDuHmRedIfIndex=_HmDuHmRedIfIndex_Object((1,3,6,1,4,1,248,14,4,1,1,5),_HmDuHmRedIfIndex_Type())
hmDuHmRedIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmDuHmRedIfIndex.setStatus(_A)
class _HmDuHmRedIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_H,2),(_K,3),(_L,4),(_I,5),(_M,6)))
_HmDuHmRedIfOpState_Type.__name__=_B
_HmDuHmRedIfOpState_Object=MibTableColumn
hmDuHmRedIfOpState=_HmDuHmRedIfOpState_Object((1,3,6,1,4,1,248,14,4,1,1,6),_HmDuHmRedIfOpState_Type())
hmDuHmRedIfOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDuHmRedIfOpState.setStatus(_A)
class _HmDuHmDesiredAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('create',1),('deactivate',2),('activate',3),('delete',4)))
_HmDuHmDesiredAction_Type.__name__=_B
_HmDuHmDesiredAction_Object=MibTableColumn
hmDuHmDesiredAction=_HmDuHmDesiredAction_Object((1,3,6,1,4,1,248,14,4,1,1,7),_HmDuHmDesiredAction_Type())
hmDuHmDesiredAction.setMaxAccess(_E)
if mibBuilder.loadTexts:hmDuHmDesiredAction.setStatus(_A)
class _HmDuHmOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('underCreation',1),('checking',2),(_H,3),(_I,4),('invalid',5),('OutOfOrder',6)))
_HmDuHmOperState_Type.__name__=_B
_HmDuHmOperState_Object=MibTableColumn
hmDuHmOperState=_HmDuHmOperState_Object((1,3,6,1,4,1,248,14,4,1,1,8),_HmDuHmOperState_Type())
hmDuHmOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDuHmOperState.setStatus(_A)
_HmDuHmPortRevivalDelay_Type=Integer32
_HmDuHmPortRevivalDelay_Object=MibTableColumn
hmDuHmPortRevivalDelay=_HmDuHmPortRevivalDelay_Object((1,3,6,1,4,1,248,14,4,1,1,9),_HmDuHmPortRevivalDelay_Type())
hmDuHmPortRevivalDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:hmDuHmPortRevivalDelay.setStatus(_A)
class _HmDuHmLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('physical',1),('layer2Frames',2)))
_HmDuHmLinkMode_Type.__name__=_B
_HmDuHmLinkMode_Object=MibTableColumn
hmDuHmLinkMode=_HmDuHmLinkMode_Object((1,3,6,1,4,1,248,14,4,1,1,10),_HmDuHmLinkMode_Type())
hmDuHmLinkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hmDuHmLinkMode.setStatus(_A)
class _HmDuHmRedCheckEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HmDuHmRedCheckEnable_Type.__name__=_B
_HmDuHmRedCheckEnable_Object=MibTableColumn
hmDuHmRedCheckEnable=_HmDuHmRedCheckEnable_Object((1,3,6,1,4,1,248,14,4,1,1,11),_HmDuHmRedCheckEnable_Type())
hmDuHmRedCheckEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hmDuHmRedCheckEnable.setStatus(_A)
class _HmDuHmRedCheckState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('failed',2)))
_HmDuHmRedCheckState_Type.__name__=_B
_HmDuHmRedCheckState_Object=MibTableColumn
hmDuHmRedCheckState=_HmDuHmRedCheckState_Object((1,3,6,1,4,1,248,14,4,1,1,12),_HmDuHmRedCheckState_Type())
hmDuHmRedCheckState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDuHmRedCheckState.setStatus(_A)
hmDuHmReconfig=NotificationType((1,3,6,1,4,1,248,14,4,0,1))
hmDuHmReconfig.setObjects(*((_C,_F),(_C,_G),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:hmDuHmReconfig.setStatus('')
hmDuHmRedundancy=NotificationType((1,3,6,1,4,1,248,14,4,0,2))
hmDuHmRedundancy.setObjects((_C,_R))
if mibBuilder.loadTexts:hmDuHmRedundancy.setStatus('')
mibBuilder.exportSymbols(_C,**{'hmDualHoming':hmDualHoming,'hmDuHmReconfig':hmDuHmReconfig,'hmDuHmRedundancy':hmDuHmRedundancy,'hmDualHomingTable':hmDualHomingTable,'hmDuHmEntry':hmDuHmEntry,_F:hmDuHmPrimGroupID,_G:hmDuHmPrimIfIndex,_N:hmDuHmPrimIfOpState,_O:hmDuHmRedGroupID,_P:hmDuHmRedIfIndex,_Q:hmDuHmRedIfOpState,'hmDuHmDesiredAction':hmDuHmDesiredAction,'hmDuHmOperState':hmDuHmOperState,'hmDuHmPortRevivalDelay':hmDuHmPortRevivalDelay,'hmDuHmLinkMode':hmDuHmLinkMode,'hmDuHmRedCheckEnable':hmDuHmRedCheckEnable,_R:hmDuHmRedCheckState})