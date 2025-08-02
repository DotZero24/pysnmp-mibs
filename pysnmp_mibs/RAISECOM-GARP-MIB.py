_L='forbidden'
_K='normal'
_J='TruthValue'
_I='Integer32'
_H='TimeInterval'
_G='EnabledStatus'
_F='EnableVar'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H,_J)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_F)
raisecomGarp=ModuleIdentity((1,3,6,1,4,1,8886,1,42))
_RaisecomGarpNotifications_ObjectIdentity=ObjectIdentity
raisecomGarpNotifications=_RaisecomGarpNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,42,0))
_RaisecomGarpCommonObjects_ObjectIdentity=ObjectIdentity
raisecomGarpCommonObjects=_RaisecomGarpCommonObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,42,1))
_RaisecomGarpPortTable_Object=MibTable
raisecomGarpPortTable=_RaisecomGarpPortTable_Object((1,3,6,1,4,1,8886,1,42,1,1))
if mibBuilder.loadTexts:raisecomGarpPortTable.setStatus(_A)
_RaisecomGarpPortEntry_Object=MibTableRow
raisecomGarpPortEntry=_RaisecomGarpPortEntry_Object((1,3,6,1,4,1,8886,1,42,1,1,1))
raisecomGarpPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:raisecomGarpPortEntry.setStatus(_A)
class _RaisecomGarpPortJoinTime_Type(TimeInterval):defaultValue=20
_RaisecomGarpPortJoinTime_Type.__name__=_H
_RaisecomGarpPortJoinTime_Object=MibTableColumn
raisecomGarpPortJoinTime=_RaisecomGarpPortJoinTime_Object((1,3,6,1,4,1,8886,1,42,1,1,1,1),_RaisecomGarpPortJoinTime_Type())
raisecomGarpPortJoinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGarpPortJoinTime.setStatus(_A)
class _RaisecomGarpPortLeaveTime_Type(TimeInterval):defaultValue=60
_RaisecomGarpPortLeaveTime_Type.__name__=_H
_RaisecomGarpPortLeaveTime_Object=MibTableColumn
raisecomGarpPortLeaveTime=_RaisecomGarpPortLeaveTime_Object((1,3,6,1,4,1,8886,1,42,1,1,1,2),_RaisecomGarpPortLeaveTime_Type())
raisecomGarpPortLeaveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGarpPortLeaveTime.setStatus(_A)
class _RaisecomGarpPortLeaveAllTime_Type(TimeInterval):defaultValue=1000
_RaisecomGarpPortLeaveAllTime_Type.__name__=_H
_RaisecomGarpPortLeaveAllTime_Object=MibTableColumn
raisecomGarpPortLeaveAllTime=_RaisecomGarpPortLeaveAllTime_Object((1,3,6,1,4,1,8886,1,42,1,1,1,3),_RaisecomGarpPortLeaveAllTime_Type())
raisecomGarpPortLeaveAllTime.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGarpPortLeaveAllTime.setStatus(_A)
class _RaisecomGarpPortStatisticClear_Type(EnableVar):defaultValue=2
_RaisecomGarpPortStatisticClear_Type.__name__=_F
_RaisecomGarpPortStatisticClear_Object=MibTableColumn
raisecomGarpPortStatisticClear=_RaisecomGarpPortStatisticClear_Object((1,3,6,1,4,1,8886,1,42,1,1,1,4),_RaisecomGarpPortStatisticClear_Type())
raisecomGarpPortStatisticClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGarpPortStatisticClear.setStatus(_A)
class _RaisecomGvrpPortStatisticClear_Type(EnableVar):defaultValue=2
_RaisecomGvrpPortStatisticClear_Type.__name__=_F
_RaisecomGvrpPortStatisticClear_Object=MibTableColumn
raisecomGvrpPortStatisticClear=_RaisecomGvrpPortStatisticClear_Object((1,3,6,1,4,1,8886,1,42,1,1,1,5),_RaisecomGvrpPortStatisticClear_Type())
raisecomGvrpPortStatisticClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGvrpPortStatisticClear.setStatus(_A)
class _RaisecomGmrpPortStatisticClear_Type(EnableVar):defaultValue=2
_RaisecomGmrpPortStatisticClear_Type.__name__=_F
_RaisecomGmrpPortStatisticClear_Object=MibTableColumn
raisecomGmrpPortStatisticClear=_RaisecomGmrpPortStatisticClear_Object((1,3,6,1,4,1,8886,1,42,1,1,1,6),_RaisecomGmrpPortStatisticClear_Type())
raisecomGmrpPortStatisticClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGmrpPortStatisticClear.setStatus(_A)
_RaisecomGarpApplicationObjects_ObjectIdentity=ObjectIdentity
raisecomGarpApplicationObjects=_RaisecomGarpApplicationObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,42,2))
_RaisecomGvrpObjects_ObjectIdentity=ObjectIdentity
raisecomGvrpObjects=_RaisecomGvrpObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,42,2,1))
class _RaisecomGvrpStatus_Type(EnabledStatus):defaultValue=2
_RaisecomGvrpStatus_Type.__name__=_G
_RaisecomGvrpStatus_Object=MibScalar
raisecomGvrpStatus=_RaisecomGvrpStatus_Object((1,3,6,1,4,1,8886,1,42,2,1,1),_RaisecomGvrpStatus_Type())
raisecomGvrpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGvrpStatus.setStatus(_A)
_RaisecomGvrpMaxVlan_Type=Integer32
_RaisecomGvrpMaxVlan_Object=MibScalar
raisecomGvrpMaxVlan=_RaisecomGvrpMaxVlan_Object((1,3,6,1,4,1,8886,1,42,2,1,2),_RaisecomGvrpMaxVlan_Type())
raisecomGvrpMaxVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpMaxVlan.setStatus(_A)
_RaisecomGvrpPortTable_Object=MibTable
raisecomGvrpPortTable=_RaisecomGvrpPortTable_Object((1,3,6,1,4,1,8886,1,42,2,1,3))
if mibBuilder.loadTexts:raisecomGvrpPortTable.setStatus(_A)
_RaisecomGvrpPortEntry_Object=MibTableRow
raisecomGvrpPortEntry=_RaisecomGvrpPortEntry_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1))
raisecomGvrpPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:raisecomGvrpPortEntry.setStatus(_A)
class _RaisecomGvrpPortStatus_Type(EnabledStatus):defaultValue=2
_RaisecomGvrpPortStatus_Type.__name__=_G
_RaisecomGvrpPortStatus_Object=MibTableColumn
raisecomGvrpPortStatus=_RaisecomGvrpPortStatus_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1,1),_RaisecomGvrpPortStatus_Type())
raisecomGvrpPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGvrpPortStatus.setStatus(_A)
_RaisecomGvrpPortLastPduOrigin_Type=MacAddress
_RaisecomGvrpPortLastPduOrigin_Object=MibTableColumn
raisecomGvrpPortLastPduOrigin=_RaisecomGvrpPortLastPduOrigin_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1,2),_RaisecomGvrpPortLastPduOrigin_Type())
raisecomGvrpPortLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpPortLastPduOrigin.setStatus(_A)
_RaisecomGvrpPortFailedRegistrations_Type=Counter32
_RaisecomGvrpPortFailedRegistrations_Object=MibTableColumn
raisecomGvrpPortFailedRegistrations=_RaisecomGvrpPortFailedRegistrations_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1,3),_RaisecomGvrpPortFailedRegistrations_Type())
raisecomGvrpPortFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpPortFailedRegistrations.setStatus(_A)
class _RaisecomGvrpPortRestrictedVlanRegistration_Type(TruthValue):defaultValue=2
_RaisecomGvrpPortRestrictedVlanRegistration_Type.__name__=_J
_RaisecomGvrpPortRestrictedVlanRegistration_Object=MibTableColumn
raisecomGvrpPortRestrictedVlanRegistration=_RaisecomGvrpPortRestrictedVlanRegistration_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1,4),_RaisecomGvrpPortRestrictedVlanRegistration_Type())
raisecomGvrpPortRestrictedVlanRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGvrpPortRestrictedVlanRegistration.setStatus(_A)
class _RaisecomGvrpPortRegistrationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('fixed',2),(_L,3)))
_RaisecomGvrpPortRegistrationMode_Type.__name__=_I
_RaisecomGvrpPortRegistrationMode_Object=MibTableColumn
raisecomGvrpPortRegistrationMode=_RaisecomGvrpPortRegistrationMode_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1,5),_RaisecomGvrpPortRegistrationMode_Type())
raisecomGvrpPortRegistrationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGvrpPortRegistrationMode.setStatus(_A)
class _RaisecomGvrpPortRunStatus_Type(EnableVar):defaultValue=2
_RaisecomGvrpPortRunStatus_Type.__name__=_F
_RaisecomGvrpPortRunStatus_Object=MibTableColumn
raisecomGvrpPortRunStatus=_RaisecomGvrpPortRunStatus_Object((1,3,6,1,4,1,8886,1,42,2,1,3,1,6),_RaisecomGvrpPortRunStatus_Type())
raisecomGvrpPortRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpPortRunStatus.setStatus(_A)
_RaisecomGvrpPortStatisticTable_Object=MibTable
raisecomGvrpPortStatisticTable=_RaisecomGvrpPortStatisticTable_Object((1,3,6,1,4,1,8886,1,42,2,1,4))
if mibBuilder.loadTexts:raisecomGvrpPortStatisticTable.setStatus(_A)
_RaisecomGvrpPortStatisticEntry_Object=MibTableRow
raisecomGvrpPortStatisticEntry=_RaisecomGvrpPortStatisticEntry_Object((1,3,6,1,4,1,8886,1,42,2,1,4,1))
raisecomGvrpPortStatisticEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:raisecomGvrpPortStatisticEntry.setStatus(_A)
_RaisecomGvrpPortFrameRx_Type=Integer32
_RaisecomGvrpPortFrameRx_Object=MibTableColumn
raisecomGvrpPortFrameRx=_RaisecomGvrpPortFrameRx_Object((1,3,6,1,4,1,8886,1,42,2,1,4,1,1),_RaisecomGvrpPortFrameRx_Type())
raisecomGvrpPortFrameRx.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpPortFrameRx.setStatus(_A)
_RaisecomGvrpPortFrameTx_Type=Integer32
_RaisecomGvrpPortFrameTx_Object=MibTableColumn
raisecomGvrpPortFrameTx=_RaisecomGvrpPortFrameTx_Object((1,3,6,1,4,1,8886,1,42,2,1,4,1,2),_RaisecomGvrpPortFrameTx_Type())
raisecomGvrpPortFrameTx.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpPortFrameTx.setStatus(_A)
_RaisecomGvrpPortFrameDiscard_Type=Integer32
_RaisecomGvrpPortFrameDiscard_Object=MibTableColumn
raisecomGvrpPortFrameDiscard=_RaisecomGvrpPortFrameDiscard_Object((1,3,6,1,4,1,8886,1,42,2,1,4,1,3),_RaisecomGvrpPortFrameDiscard_Type())
raisecomGvrpPortFrameDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGvrpPortFrameDiscard.setStatus(_A)
_RaisecomGmrpObjects_ObjectIdentity=ObjectIdentity
raisecomGmrpObjects=_RaisecomGmrpObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,42,2,2))
class _RaisecomGmrpStatus_Type(EnabledStatus):defaultValue=2
_RaisecomGmrpStatus_Type.__name__=_G
_RaisecomGmrpStatus_Object=MibScalar
raisecomGmrpStatus=_RaisecomGmrpStatus_Object((1,3,6,1,4,1,8886,1,42,2,2,1),_RaisecomGmrpStatus_Type())
raisecomGmrpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGmrpStatus.setStatus(_A)
_RaisecomGmrpMaxGroup_Type=Integer32
_RaisecomGmrpMaxGroup_Object=MibScalar
raisecomGmrpMaxGroup=_RaisecomGmrpMaxGroup_Object((1,3,6,1,4,1,8886,1,42,2,2,2),_RaisecomGmrpMaxGroup_Type())
raisecomGmrpMaxGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpMaxGroup.setStatus(_A)
_RaisecomGmrpPortTable_Object=MibTable
raisecomGmrpPortTable=_RaisecomGmrpPortTable_Object((1,3,6,1,4,1,8886,1,42,2,2,3))
if mibBuilder.loadTexts:raisecomGmrpPortTable.setStatus(_A)
_RaisecomGmrpPortEntry_Object=MibTableRow
raisecomGmrpPortEntry=_RaisecomGmrpPortEntry_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1))
raisecomGmrpPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:raisecomGmrpPortEntry.setStatus(_A)
class _RaisecomGmrpPortStatus_Type(EnabledStatus):defaultValue=1
_RaisecomGmrpPortStatus_Type.__name__=_G
_RaisecomGmrpPortStatus_Object=MibTableColumn
raisecomGmrpPortStatus=_RaisecomGmrpPortStatus_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1,1),_RaisecomGmrpPortStatus_Type())
raisecomGmrpPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGmrpPortStatus.setStatus(_A)
_RaisecomGmrpPortFailedRegistrations_Type=Counter32
_RaisecomGmrpPortFailedRegistrations_Object=MibTableColumn
raisecomGmrpPortFailedRegistrations=_RaisecomGmrpPortFailedRegistrations_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1,2),_RaisecomGmrpPortFailedRegistrations_Type())
raisecomGmrpPortFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpPortFailedRegistrations.setStatus(_A)
_RaisecomGmrpPortLastPduOrigin_Type=MacAddress
_RaisecomGmrpPortLastPduOrigin_Object=MibTableColumn
raisecomGmrpPortLastPduOrigin=_RaisecomGmrpPortLastPduOrigin_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1,3),_RaisecomGmrpPortLastPduOrigin_Type())
raisecomGmrpPortLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpPortLastPduOrigin.setStatus(_A)
class _RaisecomGmrpPortRestrictedGroupRegistration_Type(TruthValue):defaultValue=2
_RaisecomGmrpPortRestrictedGroupRegistration_Type.__name__=_J
_RaisecomGmrpPortRestrictedGroupRegistration_Object=MibTableColumn
raisecomGmrpPortRestrictedGroupRegistration=_RaisecomGmrpPortRestrictedGroupRegistration_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1,4),_RaisecomGmrpPortRestrictedGroupRegistration_Type())
raisecomGmrpPortRestrictedGroupRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGmrpPortRestrictedGroupRegistration.setStatus(_A)
class _RaisecomGmrpPortRegistrationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('fixed',2),(_L,3)))
_RaisecomGmrpPortRegistrationMode_Type.__name__=_I
_RaisecomGmrpPortRegistrationMode_Object=MibTableColumn
raisecomGmrpPortRegistrationMode=_RaisecomGmrpPortRegistrationMode_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1,5),_RaisecomGmrpPortRegistrationMode_Type())
raisecomGmrpPortRegistrationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomGmrpPortRegistrationMode.setStatus(_A)
class _RaisecomGmrpPortRunStatus_Type(EnableVar):defaultValue=2
_RaisecomGmrpPortRunStatus_Type.__name__=_F
_RaisecomGmrpPortRunStatus_Object=MibTableColumn
raisecomGmrpPortRunStatus=_RaisecomGmrpPortRunStatus_Object((1,3,6,1,4,1,8886,1,42,2,2,3,1,6),_RaisecomGmrpPortRunStatus_Type())
raisecomGmrpPortRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpPortRunStatus.setStatus(_A)
_RaisecomGmrpPortStatisticTable_Object=MibTable
raisecomGmrpPortStatisticTable=_RaisecomGmrpPortStatisticTable_Object((1,3,6,1,4,1,8886,1,42,2,2,4))
if mibBuilder.loadTexts:raisecomGmrpPortStatisticTable.setStatus(_A)
_RaisecomGmrpPortStatisticEntry_Object=MibTableRow
raisecomGmrpPortStatisticEntry=_RaisecomGmrpPortStatisticEntry_Object((1,3,6,1,4,1,8886,1,42,2,2,4,1))
raisecomGmrpPortStatisticEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:raisecomGmrpPortStatisticEntry.setStatus(_A)
_RaisecomGmrpPortFrameRx_Type=Integer32
_RaisecomGmrpPortFrameRx_Object=MibTableColumn
raisecomGmrpPortFrameRx=_RaisecomGmrpPortFrameRx_Object((1,3,6,1,4,1,8886,1,42,2,2,4,1,1),_RaisecomGmrpPortFrameRx_Type())
raisecomGmrpPortFrameRx.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpPortFrameRx.setStatus(_A)
_RaisecomGmrpPortFrameTx_Type=Integer32
_RaisecomGmrpPortFrameTx_Object=MibTableColumn
raisecomGmrpPortFrameTx=_RaisecomGmrpPortFrameTx_Object((1,3,6,1,4,1,8886,1,42,2,2,4,1,2),_RaisecomGmrpPortFrameTx_Type())
raisecomGmrpPortFrameTx.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpPortFrameTx.setStatus(_A)
_RaisecomGmrpPortFrameDiscard_Type=Integer32
_RaisecomGmrpPortFrameDiscard_Object=MibTableColumn
raisecomGmrpPortFrameDiscard=_RaisecomGmrpPortFrameDiscard_Object((1,3,6,1,4,1,8886,1,42,2,2,4,1,3),_RaisecomGmrpPortFrameDiscard_Type())
raisecomGmrpPortFrameDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomGmrpPortFrameDiscard.setStatus(_A)
_RaisecomGarpConformance_ObjectIdentity=ObjectIdentity
raisecomGarpConformance=_RaisecomGarpConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,42,3))
mibBuilder.exportSymbols('RAISECOM-GARP-MIB',**{'raisecomGarp':raisecomGarp,'raisecomGarpNotifications':raisecomGarpNotifications,'raisecomGarpCommonObjects':raisecomGarpCommonObjects,'raisecomGarpPortTable':raisecomGarpPortTable,'raisecomGarpPortEntry':raisecomGarpPortEntry,'raisecomGarpPortJoinTime':raisecomGarpPortJoinTime,'raisecomGarpPortLeaveTime':raisecomGarpPortLeaveTime,'raisecomGarpPortLeaveAllTime':raisecomGarpPortLeaveAllTime,'raisecomGarpPortStatisticClear':raisecomGarpPortStatisticClear,'raisecomGvrpPortStatisticClear':raisecomGvrpPortStatisticClear,'raisecomGmrpPortStatisticClear':raisecomGmrpPortStatisticClear,'raisecomGarpApplicationObjects':raisecomGarpApplicationObjects,'raisecomGvrpObjects':raisecomGvrpObjects,'raisecomGvrpStatus':raisecomGvrpStatus,'raisecomGvrpMaxVlan':raisecomGvrpMaxVlan,'raisecomGvrpPortTable':raisecomGvrpPortTable,'raisecomGvrpPortEntry':raisecomGvrpPortEntry,'raisecomGvrpPortStatus':raisecomGvrpPortStatus,'raisecomGvrpPortLastPduOrigin':raisecomGvrpPortLastPduOrigin,'raisecomGvrpPortFailedRegistrations':raisecomGvrpPortFailedRegistrations,'raisecomGvrpPortRestrictedVlanRegistration':raisecomGvrpPortRestrictedVlanRegistration,'raisecomGvrpPortRegistrationMode':raisecomGvrpPortRegistrationMode,'raisecomGvrpPortRunStatus':raisecomGvrpPortRunStatus,'raisecomGvrpPortStatisticTable':raisecomGvrpPortStatisticTable,'raisecomGvrpPortStatisticEntry':raisecomGvrpPortStatisticEntry,'raisecomGvrpPortFrameRx':raisecomGvrpPortFrameRx,'raisecomGvrpPortFrameTx':raisecomGvrpPortFrameTx,'raisecomGvrpPortFrameDiscard':raisecomGvrpPortFrameDiscard,'raisecomGmrpObjects':raisecomGmrpObjects,'raisecomGmrpStatus':raisecomGmrpStatus,'raisecomGmrpMaxGroup':raisecomGmrpMaxGroup,'raisecomGmrpPortTable':raisecomGmrpPortTable,'raisecomGmrpPortEntry':raisecomGmrpPortEntry,'raisecomGmrpPortStatus':raisecomGmrpPortStatus,'raisecomGmrpPortFailedRegistrations':raisecomGmrpPortFailedRegistrations,'raisecomGmrpPortLastPduOrigin':raisecomGmrpPortLastPduOrigin,'raisecomGmrpPortRestrictedGroupRegistration':raisecomGmrpPortRestrictedGroupRegistration,'raisecomGmrpPortRegistrationMode':raisecomGmrpPortRegistrationMode,'raisecomGmrpPortRunStatus':raisecomGmrpPortRunStatus,'raisecomGmrpPortStatisticTable':raisecomGmrpPortStatisticTable,'raisecomGmrpPortStatisticEntry':raisecomGmrpPortStatisticEntry,'raisecomGmrpPortFrameRx':raisecomGmrpPortFrameRx,'raisecomGmrpPortFrameTx':raisecomGmrpPortFrameTx,'raisecomGmrpPortFrameDiscard':raisecomGmrpPortFrameDiscard,'raisecomGarpConformance':raisecomGarpConformance})