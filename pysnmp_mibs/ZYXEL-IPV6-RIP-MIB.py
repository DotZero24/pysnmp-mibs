_E='zyIpv6IfIndex'
_D='ZYXEL-IPV6-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyIpv6IfIndex,=mibBuilder.importSymbols(_D,_E)
zyxelIpv6Rip=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,115))
_ZyxelIpv6RipSetup_ObjectIdentity=ObjectIdentity
zyxelIpv6RipSetup=_ZyxelIpv6RipSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,115,1))
_ZyIpv6RipState_Type=EnabledStatus
_ZyIpv6RipState_Object=MibScalar
zyIpv6RipState=_ZyIpv6RipState_Object((1,3,6,1,4,1,890,1,15,3,115,1,1),_ZyIpv6RipState_Type())
zyIpv6RipState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipState.setStatus(_A)
class _ZyIpv6RipUpdateTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZyIpv6RipUpdateTimer_Type.__name__=_C
_ZyIpv6RipUpdateTimer_Object=MibScalar
zyIpv6RipUpdateTimer=_ZyIpv6RipUpdateTimer_Object((1,3,6,1,4,1,890,1,15,3,115,1,2),_ZyIpv6RipUpdateTimer_Type())
zyIpv6RipUpdateTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipUpdateTimer.setStatus(_A)
class _ZyIpv6RipTimeoutTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZyIpv6RipTimeoutTimer_Type.__name__=_C
_ZyIpv6RipTimeoutTimer_Object=MibScalar
zyIpv6RipTimeoutTimer=_ZyIpv6RipTimeoutTimer_Object((1,3,6,1,4,1,890,1,15,3,115,1,3),_ZyIpv6RipTimeoutTimer_Type())
zyIpv6RipTimeoutTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipTimeoutTimer.setStatus(_A)
class _ZyIpv6RipGarbageCollectionTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZyIpv6RipGarbageCollectionTimer_Type.__name__=_C
_ZyIpv6RipGarbageCollectionTimer_Object=MibScalar
zyIpv6RipGarbageCollectionTimer=_ZyIpv6RipGarbageCollectionTimer_Object((1,3,6,1,4,1,890,1,15,3,115,1,4),_ZyIpv6RipGarbageCollectionTimer_Type())
zyIpv6RipGarbageCollectionTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipGarbageCollectionTimer.setStatus(_A)
class _ZyIpv6RipDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_ZyIpv6RipDistance_Type.__name__=_C
_ZyIpv6RipDistance_Object=MibScalar
zyIpv6RipDistance=_ZyIpv6RipDistance_Object((1,3,6,1,4,1,890,1,15,3,115,1,5),_ZyIpv6RipDistance_Type())
zyIpv6RipDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipDistance.setStatus(_A)
_ZyxelIpv6RipInterfaceTable_Object=MibTable
zyxelIpv6RipInterfaceTable=_ZyxelIpv6RipInterfaceTable_Object((1,3,6,1,4,1,890,1,15,3,115,1,6))
if mibBuilder.loadTexts:zyxelIpv6RipInterfaceTable.setStatus(_A)
_ZyxelIpv6RipInterfaceEntry_Object=MibTableRow
zyxelIpv6RipInterfaceEntry=_ZyxelIpv6RipInterfaceEntry_Object((1,3,6,1,4,1,890,1,15,3,115,1,6,1))
zyxelIpv6RipInterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelIpv6RipInterfaceEntry.setStatus(_A)
_ZyIpv6RipInterfaceState_Type=EnabledStatus
_ZyIpv6RipInterfaceState_Object=MibTableColumn
zyIpv6RipInterfaceState=_ZyIpv6RipInterfaceState_Object((1,3,6,1,4,1,890,1,15,3,115,1,6,1,1),_ZyIpv6RipInterfaceState_Type())
zyIpv6RipInterfaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipInterfaceState.setStatus(_A)
class _ZyIpv6RipInterfaceMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ZyIpv6RipInterfaceMetric_Type.__name__=_C
_ZyIpv6RipInterfaceMetric_Object=MibTableColumn
zyIpv6RipInterfaceMetric=_ZyIpv6RipInterfaceMetric_Object((1,3,6,1,4,1,890,1,15,3,115,1,6,1,2),_ZyIpv6RipInterfaceMetric_Type())
zyIpv6RipInterfaceMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipInterfaceMetric.setStatus(_A)
class _ZyIpv6RipInterfaceMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no_horizon',1),('split_horizon',2),('poison_reverse',3)))
_ZyIpv6RipInterfaceMethod_Type.__name__=_C
_ZyIpv6RipInterfaceMethod_Object=MibTableColumn
zyIpv6RipInterfaceMethod=_ZyIpv6RipInterfaceMethod_Object((1,3,6,1,4,1,890,1,15,3,115,1,6,1,3),_ZyIpv6RipInterfaceMethod_Type())
zyIpv6RipInterfaceMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6RipInterfaceMethod.setStatus(_A)
_ZyxelIpv6RipNotifications_ObjectIdentity=ObjectIdentity
zyxelIpv6RipNotifications=_ZyxelIpv6RipNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,115,4))
zyIpv6RipExceedMaxDynamicRoute=NotificationType((1,3,6,1,4,1,890,1,15,3,115,4,1))
if mibBuilder.loadTexts:zyIpv6RipExceedMaxDynamicRoute.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-IPV6-RIP-MIB',**{'zyxelIpv6Rip':zyxelIpv6Rip,'zyxelIpv6RipSetup':zyxelIpv6RipSetup,'zyIpv6RipState':zyIpv6RipState,'zyIpv6RipUpdateTimer':zyIpv6RipUpdateTimer,'zyIpv6RipTimeoutTimer':zyIpv6RipTimeoutTimer,'zyIpv6RipGarbageCollectionTimer':zyIpv6RipGarbageCollectionTimer,'zyIpv6RipDistance':zyIpv6RipDistance,'zyxelIpv6RipInterfaceTable':zyxelIpv6RipInterfaceTable,'zyxelIpv6RipInterfaceEntry':zyxelIpv6RipInterfaceEntry,'zyIpv6RipInterfaceState':zyIpv6RipInterfaceState,'zyIpv6RipInterfaceMetric':zyIpv6RipInterfaceMetric,'zyIpv6RipInterfaceMethod':zyIpv6RipInterfaceMethod,'zyxelIpv6RipNotifications':zyxelIpv6RipNotifications,'zyIpv6RipExceedMaxDynamicRoute':zyIpv6RipExceedMaxDynamicRoute})