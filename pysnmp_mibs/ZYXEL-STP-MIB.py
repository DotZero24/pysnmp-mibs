_L='zyStpRootGuardInstance'
_K='zyStpMode'
_J='zyMstpInstanceId'
_I='ZYXEL-MSTP-MIB'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='ZYXEL-STP-MIB'
_D='read-write'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
ifIndex,=mibBuilder.importSymbols(_F,_G)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyMstpInstanceId,=mibBuilder.importSymbols(_I,_J)
zyxelStp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,79))
class MstiOrCistInstanceIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ZyxelStpSetup_ObjectIdentity=ObjectIdentity
zyxelStpSetup=_ZyxelStpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,79,1))
class _ZyStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rstp',1),('mrstp',2),('mstp',3)))
_ZyStpMode_Type.__name__=_H
_ZyStpMode_Object=MibScalar
zyStpMode=_ZyStpMode_Object((1,3,6,1,4,1,890,1,15,3,79,1,1),_ZyStpMode_Type())
zyStpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zyStpMode.setStatus(_A)
_ZyStpRstpState_Type=EnabledStatus
_ZyStpRstpState_Object=MibScalar
zyStpRstpState=_ZyStpRstpState_Object((1,3,6,1,4,1,890,1,15,3,79,1,2),_ZyStpRstpState_Type())
zyStpRstpState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyStpRstpState.setStatus(_A)
_ZyxelStpRootGuardRstpTable_Object=MibTable
zyxelStpRootGuardRstpTable=_ZyxelStpRootGuardRstpTable_Object((1,3,6,1,4,1,890,1,15,3,79,1,3))
if mibBuilder.loadTexts:zyxelStpRootGuardRstpTable.setStatus(_A)
_ZyxelStpRootGuardRstpPortEntry_Object=MibTableRow
zyxelStpRootGuardRstpPortEntry=_ZyxelStpRootGuardRstpPortEntry_Object((1,3,6,1,4,1,890,1,15,3,79,1,3,1))
zyxelStpRootGuardRstpPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelStpRootGuardRstpPortEntry.setStatus(_A)
_ZyStpRootGuardRstpState_Type=EnabledStatus
_ZyStpRootGuardRstpState_Object=MibTableColumn
zyStpRootGuardRstpState=_ZyStpRootGuardRstpState_Object((1,3,6,1,4,1,890,1,15,3,79,1,3,1,1),_ZyStpRootGuardRstpState_Type())
zyStpRootGuardRstpState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyStpRootGuardRstpState.setStatus(_A)
_ZyxelStpRootGuardMrstpTable_Object=MibTable
zyxelStpRootGuardMrstpTable=_ZyxelStpRootGuardMrstpTable_Object((1,3,6,1,4,1,890,1,15,3,79,1,4))
if mibBuilder.loadTexts:zyxelStpRootGuardMrstpTable.setStatus(_A)
_ZyxelStpRootGuardMrstpPortEntry_Object=MibTableRow
zyxelStpRootGuardMrstpPortEntry=_ZyxelStpRootGuardMrstpPortEntry_Object((1,3,6,1,4,1,890,1,15,3,79,1,4,1))
zyxelStpRootGuardMrstpPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelStpRootGuardMrstpPortEntry.setStatus(_A)
_ZyStpRootGuardMrstpState_Type=EnabledStatus
_ZyStpRootGuardMrstpState_Object=MibTableColumn
zyStpRootGuardMrstpState=_ZyStpRootGuardMrstpState_Object((1,3,6,1,4,1,890,1,15,3,79,1,4,1,1),_ZyStpRootGuardMrstpState_Type())
zyStpRootGuardMrstpState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyStpRootGuardMrstpState.setStatus(_A)
_ZyxelStpRootGuardMstpTable_Object=MibTable
zyxelStpRootGuardMstpTable=_ZyxelStpRootGuardMstpTable_Object((1,3,6,1,4,1,890,1,15,3,79,1,5))
if mibBuilder.loadTexts:zyxelStpRootGuardMstpTable.setStatus(_A)
_ZyxelStpRootGuardMstpPortEntry_Object=MibTableRow
zyxelStpRootGuardMstpPortEntry=_ZyxelStpRootGuardMstpPortEntry_Object((1,3,6,1,4,1,890,1,15,3,79,1,5,1))
zyxelStpRootGuardMstpPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelStpRootGuardMstpPortEntry.setStatus(_A)
_ZyStpRootGuardMstpState_Type=EnabledStatus
_ZyStpRootGuardMstpState_Object=MibTableColumn
zyStpRootGuardMstpState=_ZyStpRootGuardMstpState_Object((1,3,6,1,4,1,890,1,15,3,79,1,5,1,1),_ZyStpRootGuardMstpState_Type())
zyStpRootGuardMstpState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyStpRootGuardMstpState.setStatus(_A)
_ZyxelStpStatus_ObjectIdentity=ObjectIdentity
zyxelStpStatus=_ZyxelStpStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,79,2))
_ZyxelStpRootGuardTable_Object=MibTable
zyxelStpRootGuardTable=_ZyxelStpRootGuardTable_Object((1,3,6,1,4,1,890,1,15,3,79,2,1))
if mibBuilder.loadTexts:zyxelStpRootGuardTable.setStatus(_A)
_ZyxelStpRootGuardEntry_Object=MibTableRow
zyxelStpRootGuardEntry=_ZyxelStpRootGuardEntry_Object((1,3,6,1,4,1,890,1,15,3,79,2,1,1))
zyxelStpRootGuardEntry.setIndexNames((0,_E,_L),(0,_B,_C))
if mibBuilder.loadTexts:zyxelStpRootGuardEntry.setStatus(_A)
_ZyStpRootGuardInstance_Type=MstiOrCistInstanceIndex
_ZyStpRootGuardInstance_Object=MibTableColumn
zyStpRootGuardInstance=_ZyStpRootGuardInstance_Object((1,3,6,1,4,1,890,1,15,3,79,2,1,1,1),_ZyStpRootGuardInstance_Type())
zyStpRootGuardInstance.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyStpRootGuardInstance.setStatus(_A)
class _ZyStpRootGuardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('forwarding',0),('rootInconsistent',1)))
_ZyStpRootGuardStatus_Type.__name__=_H
_ZyStpRootGuardStatus_Object=MibTableColumn
zyStpRootGuardStatus=_ZyStpRootGuardStatus_Object((1,3,6,1,4,1,890,1,15,3,79,2,1,1,2),_ZyStpRootGuardStatus_Type())
zyStpRootGuardStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyStpRootGuardStatus.setStatus(_A)
_ZyxelStpNotifications_ObjectIdentity=ObjectIdentity
zyxelStpNotifications=_ZyxelStpNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,79,3))
zyStpRootGuardDetect=NotificationType((1,3,6,1,4,1,890,1,15,3,79,3,1))
zyStpRootGuardDetect.setObjects(*((_E,_K),(_I,_J),(_F,_G)))
if mibBuilder.loadTexts:zyStpRootGuardDetect.setStatus(_A)
zyStpRootGuardRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,79,3,2))
zyStpRootGuardRecovered.setObjects(*((_E,_K),(_I,_J),(_F,_G)))
if mibBuilder.loadTexts:zyStpRootGuardRecovered.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MstiOrCistInstanceIndex':MstiOrCistInstanceIndex,'zyxelStp':zyxelStp,'zyxelStpSetup':zyxelStpSetup,_K:zyStpMode,'zyStpRstpState':zyStpRstpState,'zyxelStpRootGuardRstpTable':zyxelStpRootGuardRstpTable,'zyxelStpRootGuardRstpPortEntry':zyxelStpRootGuardRstpPortEntry,'zyStpRootGuardRstpState':zyStpRootGuardRstpState,'zyxelStpRootGuardMrstpTable':zyxelStpRootGuardMrstpTable,'zyxelStpRootGuardMrstpPortEntry':zyxelStpRootGuardMrstpPortEntry,'zyStpRootGuardMrstpState':zyStpRootGuardMrstpState,'zyxelStpRootGuardMstpTable':zyxelStpRootGuardMstpTable,'zyxelStpRootGuardMstpPortEntry':zyxelStpRootGuardMstpPortEntry,'zyStpRootGuardMstpState':zyStpRootGuardMstpState,'zyxelStpStatus':zyxelStpStatus,'zyxelStpRootGuardTable':zyxelStpRootGuardTable,'zyxelStpRootGuardEntry':zyxelStpRootGuardEntry,_L:zyStpRootGuardInstance,'zyStpRootGuardStatus':zyStpRootGuardStatus,'zyxelStpNotifications':zyxelStpNotifications,'zyStpRootGuardDetect':zyStpRootGuardDetect,'zyStpRootGuardRecovered':zyStpRootGuardRecovered})