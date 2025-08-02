_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsarp=ModuleIdentity((1,3,6,1,4,1,2076,109))
if mibBuilder.loadTexts:fsarp.setRevisions(('2012-09-04 00:00',))
_Arp_ObjectIdentity=ObjectIdentity
arp=_Arp_ObjectIdentity((1,3,6,1,4,1,2076,109,1))
class _FsArpCacheTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_FsArpCacheTimeout_Type.__name__=_B
_FsArpCacheTimeout_Object=MibScalar
fsArpCacheTimeout=_FsArpCacheTimeout_Object((1,3,6,1,4,1,2076,109,1,1),_FsArpCacheTimeout_Type())
fsArpCacheTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpCacheTimeout.setStatus(_A)
class _FsArpCachePendTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3000))
_FsArpCachePendTime_Type.__name__=_B
_FsArpCachePendTime_Object=MibScalar
fsArpCachePendTime=_FsArpCachePendTime_Object((1,3,6,1,4,1,2076,109,1,2),_FsArpCachePendTime_Type())
fsArpCachePendTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpCachePendTime.setStatus(_A)
class _FsArpMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_FsArpMaxRetries_Type.__name__=_B
_FsArpMaxRetries_Object=MibScalar
fsArpMaxRetries=_FsArpMaxRetries_Object((1,3,6,1,4,1,2076,109,1,3),_FsArpMaxRetries_Type())
fsArpMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpMaxRetries.setStatus(_A)
_Arptest_ObjectIdentity=ObjectIdentity
arptest=_Arptest_ObjectIdentity((1,3,6,1,4,1,2076,109,2))
_FsArpPendingEntryCount_Type=Integer32
_FsArpPendingEntryCount_Object=MibScalar
fsArpPendingEntryCount=_FsArpPendingEntryCount_Object((1,3,6,1,4,1,2076,109,2,1),_FsArpPendingEntryCount_Type())
fsArpPendingEntryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsArpPendingEntryCount.setStatus(_A)
_FsArpCacheEntryCount_Type=Integer32
_FsArpCacheEntryCount_Object=MibScalar
fsArpCacheEntryCount=_FsArpCacheEntryCount_Object((1,3,6,1,4,1,2076,109,2,2),_FsArpCacheEntryCount_Type())
fsArpCacheEntryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsArpCacheEntryCount.setStatus(_A)
_FsArpRedEntryTime_Type=Integer32
_FsArpRedEntryTime_Object=MibScalar
fsArpRedEntryTime=_FsArpRedEntryTime_Object((1,3,6,1,4,1,2076,109,2,3),_FsArpRedEntryTime_Type())
fsArpRedEntryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsArpRedEntryTime.setStatus(_A)
_FsArpRedExitTime_Type=Integer32
_FsArpRedExitTime_Object=MibScalar
fsArpRedExitTime=_FsArpRedExitTime_Object((1,3,6,1,4,1,2076,109,2,4),_FsArpRedExitTime_Type())
fsArpRedExitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsArpRedExitTime.setStatus(_A)
_FsArpCacheFlushStatus_Type=TruthValue
_FsArpCacheFlushStatus_Object=MibScalar
fsArpCacheFlushStatus=_FsArpCacheFlushStatus_Object((1,3,6,1,4,1,2076,109,2,5),_FsArpCacheFlushStatus_Type())
fsArpCacheFlushStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpCacheFlushStatus.setStatus(_A)
class _FsArpGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsArpGlobalDebug_Type.__name__=_B
_FsArpGlobalDebug_Object=MibScalar
fsArpGlobalDebug=_FsArpGlobalDebug_Object((1,3,6,1,4,1,2076,109,2,6),_FsArpGlobalDebug_Type())
fsArpGlobalDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpGlobalDebug.setStatus(_A)
mibBuilder.exportSymbols('ARICENT-ARP-MIB',**{'fsarp':fsarp,'arp':arp,'fsArpCacheTimeout':fsArpCacheTimeout,'fsArpCachePendTime':fsArpCachePendTime,'fsArpMaxRetries':fsArpMaxRetries,'arptest':arptest,'fsArpPendingEntryCount':fsArpPendingEntryCount,'fsArpCacheEntryCount':fsArpCacheEntryCount,'fsArpRedEntryTime':fsArpRedEntryTime,'fsArpRedExitTime':fsArpRedExitTime,'fsArpCacheFlushStatus':fsArpCacheFlushStatus,'fsArpGlobalDebug':fsArpGlobalDebug})