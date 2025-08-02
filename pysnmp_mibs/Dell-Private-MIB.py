_E='rlGlobalIpAdIndex'
_D='Dell-Private-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
ipAddrEntry,=mibBuilder.importSymbols('IP-MIB','ipAddrEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlOperationalMode=ModuleIdentity((1,3,6,1,4,1,89,121))
if mibBuilder.loadTexts:rlOperationalMode.setRevisions(('2006-11-01 00:00',))
class _RlOperationalModeState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('managed',0),('unmanaged',1),('secure',2)))
_RlOperationalModeState_Type.__name__=_C
_RlOperationalModeState_Object=MibScalar
rlOperationalModeState=_RlOperationalModeState_Object((1,3,6,1,4,1,89,121,1),_RlOperationalModeState_Type())
rlOperationalModeState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOperationalModeState.setStatus(_A)
_RlGlobalIpAddrTable_Object=MibTable
rlGlobalIpAddrTable=_RlGlobalIpAddrTable_Object((1,3,6,1,4,1,89,121,2))
if mibBuilder.loadTexts:rlGlobalIpAddrTable.setStatus(_A)
_RlGlobalIpAddrEntry_Object=MibTableRow
rlGlobalIpAddrEntry=_RlGlobalIpAddrEntry_Object((1,3,6,1,4,1,89,121,2,1))
rlGlobalIpAddrEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlGlobalIpAddrEntry.setStatus(_A)
class _RlGlobalIpAdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_RlGlobalIpAdIndex_Type.__name__=_C
_RlGlobalIpAdIndex_Object=MibTableColumn
rlGlobalIpAdIndex=_RlGlobalIpAdIndex_Object((1,3,6,1,4,1,89,121,2,1,1),_RlGlobalIpAdIndex_Type())
rlGlobalIpAdIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlGlobalIpAdIndex.setStatus(_A)
_RlGlobalIpAdEntAddr_Type=IpAddress
_RlGlobalIpAdEntAddr_Object=MibTableColumn
rlGlobalIpAdEntAddr=_RlGlobalIpAdEntAddr_Object((1,3,6,1,4,1,89,121,2,1,2),_RlGlobalIpAdEntAddr_Type())
rlGlobalIpAdEntAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGlobalIpAdEntAddr.setStatus(_A)
_RlGlobalIpAdEntNetMask_Type=IpAddress
_RlGlobalIpAdEntNetMask_Object=MibTableColumn
rlGlobalIpAdEntNetMask=_RlGlobalIpAdEntNetMask_Object((1,3,6,1,4,1,89,121,2,1,3),_RlGlobalIpAdEntNetMask_Type())
rlGlobalIpAdEntNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGlobalIpAdEntNetMask.setStatus(_A)
_RlGlobalIpAdDefaultGateway_Type=IpAddress
_RlGlobalIpAdDefaultGateway_Object=MibTableColumn
rlGlobalIpAdDefaultGateway=_RlGlobalIpAdDefaultGateway_Object((1,3,6,1,4,1,89,121,2,1,4),_RlGlobalIpAdDefaultGateway_Type())
rlGlobalIpAdDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGlobalIpAdDefaultGateway.setStatus(_A)
class _RlGlobalIpAdOwner_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dhcp',2),('default',3)))
_RlGlobalIpAdOwner_Type.__name__=_C
_RlGlobalIpAdOwner_Object=MibTableColumn
rlGlobalIpAdOwner=_RlGlobalIpAdOwner_Object((1,3,6,1,4,1,89,121,2,1,5),_RlGlobalIpAdOwner_Type())
rlGlobalIpAdOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGlobalIpAdOwner.setStatus(_A)
class _RlDeleteUsersAfterReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_RlDeleteUsersAfterReset_Type.__name__=_C
_RlDeleteUsersAfterReset_Object=MibScalar
rlDeleteUsersAfterReset=_RlDeleteUsersAfterReset_Object((1,3,6,1,4,1,89,121,3),_RlDeleteUsersAfterReset_Type())
rlDeleteUsersAfterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDeleteUsersAfterReset.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rlOperationalMode':rlOperationalMode,'rlOperationalModeState':rlOperationalModeState,'rlGlobalIpAddrTable':rlGlobalIpAddrTable,'rlGlobalIpAddrEntry':rlGlobalIpAddrEntry,_E:rlGlobalIpAdIndex,'rlGlobalIpAdEntAddr':rlGlobalIpAdEntAddr,'rlGlobalIpAdEntNetMask':rlGlobalIpAdEntNetMask,'rlGlobalIpAdDefaultGateway':rlGlobalIpAdDefaultGateway,'rlGlobalIpAdOwner':rlGlobalIpAdOwner,'rlDeleteUsersAfterReset':rlDeleteUsersAfterReset})