_E='Integer32'
_D='read-only'
_C='efpAgentCpuTrafficRateLimitQueueNumber'
_B='ELTEX-FASTPATH-SWITCHING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesFastpath,=mibBuilder.importSymbols('ELTEX-MES-FASTPATH-MIB','eltMesFastpath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltFastpathSwitchingMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,103,5))
if mibBuilder.loadTexts:eltFastpathSwitchingMIB.setRevisions(('2018-02-26 00:00',))
_EfpSwitchingObjects_ObjectIdentity=ObjectIdentity
efpSwitchingObjects=_EfpSwitchingObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,1))
_EfpSwitchingCpuTrafficGlobals_ObjectIdentity=ObjectIdentity
efpSwitchingCpuTrafficGlobals=_EfpSwitchingCpuTrafficGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,1,1))
_EfpSwitchingCpuTrafficConfigs_ObjectIdentity=ObjectIdentity
efpSwitchingCpuTrafficConfigs=_EfpSwitchingCpuTrafficConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,1,2))
_EfpAgentCpuTrafficRateLimitQueueTable_Object=MibTable
efpAgentCpuTrafficRateLimitQueueTable=_EfpAgentCpuTrafficRateLimitQueueTable_Object((1,3,6,1,4,1,35265,1,103,5,1,2,1))
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueTable.setStatus(_A)
_EfpAgentCpuTrafficRateLimitQueueEntry_Object=MibTableRow
efpAgentCpuTrafficRateLimitQueueEntry=_EfpAgentCpuTrafficRateLimitQueueEntry_Object((1,3,6,1,4,1,35265,1,103,5,1,2,1,1))
efpAgentCpuTrafficRateLimitQueueEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueEntry.setStatus(_A)
_EfpAgentCpuTrafficRateLimitQueueNumber_Type=Integer32
_EfpAgentCpuTrafficRateLimitQueueNumber_Object=MibTableColumn
efpAgentCpuTrafficRateLimitQueueNumber=_EfpAgentCpuTrafficRateLimitQueueNumber_Object((1,3,6,1,4,1,35265,1,103,5,1,2,1,1,1),_EfpAgentCpuTrafficRateLimitQueueNumber_Type())
efpAgentCpuTrafficRateLimitQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueNumber.setStatus(_A)
class _EfpAgentCpuTrafficRateLimitQueueLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2048))
_EfpAgentCpuTrafficRateLimitQueueLimit_Type.__name__=_E
_EfpAgentCpuTrafficRateLimitQueueLimit_Object=MibTableColumn
efpAgentCpuTrafficRateLimitQueueLimit=_EfpAgentCpuTrafficRateLimitQueueLimit_Object((1,3,6,1,4,1,35265,1,103,5,1,2,1,1,2),_EfpAgentCpuTrafficRateLimitQueueLimit_Type())
efpAgentCpuTrafficRateLimitQueueLimit.setMaxAccess('read-write')
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueLimit.setStatus(_A)
_EfpSwitchingCpuTrafficStatistics_ObjectIdentity=ObjectIdentity
efpSwitchingCpuTrafficStatistics=_EfpSwitchingCpuTrafficStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,1,3))
_EfpAgentCpuTrafficRateLimitQueueStatTable_Object=MibTable
efpAgentCpuTrafficRateLimitQueueStatTable=_EfpAgentCpuTrafficRateLimitQueueStatTable_Object((1,3,6,1,4,1,35265,1,103,5,1,3,1))
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueStatTable.setStatus(_A)
_EfpAgentCpuTrafficRateLimitQueueStatEntry_Object=MibTableRow
efpAgentCpuTrafficRateLimitQueueStatEntry=_EfpAgentCpuTrafficRateLimitQueueStatEntry_Object((1,3,6,1,4,1,35265,1,103,5,1,3,1,1))
efpAgentCpuTrafficRateLimitQueueStatEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueStatEntry.setStatus(_A)
_EfpAgentCpuTrafficRateLimitQueueRate_Type=Integer32
_EfpAgentCpuTrafficRateLimitQueueRate_Object=MibTableColumn
efpAgentCpuTrafficRateLimitQueueRate=_EfpAgentCpuTrafficRateLimitQueueRate_Object((1,3,6,1,4,1,35265,1,103,5,1,3,1,1,1),_EfpAgentCpuTrafficRateLimitQueueRate_Type())
efpAgentCpuTrafficRateLimitQueueRate.setMaxAccess(_D)
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueueRate.setStatus(_A)
_EfpAgentCpuTrafficRateLimitQueuePackets_Type=Integer32
_EfpAgentCpuTrafficRateLimitQueuePackets_Object=MibTableColumn
efpAgentCpuTrafficRateLimitQueuePackets=_EfpAgentCpuTrafficRateLimitQueuePackets_Object((1,3,6,1,4,1,35265,1,103,5,1,3,1,1,2),_EfpAgentCpuTrafficRateLimitQueuePackets_Type())
efpAgentCpuTrafficRateLimitQueuePackets.setMaxAccess(_D)
if mibBuilder.loadTexts:efpAgentCpuTrafficRateLimitQueuePackets.setStatus(_A)
_EfpSwitchingNotifications_ObjectIdentity=ObjectIdentity
efpSwitchingNotifications=_EfpSwitchingNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,2))
_EfpSwitchingNotificationsPrefix_ObjectIdentity=ObjectIdentity
efpSwitchingNotificationsPrefix=_EfpSwitchingNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,2,0))
_EfpSwitchingConformance_ObjectIdentity=ObjectIdentity
efpSwitchingConformance=_EfpSwitchingConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,3))
_EfpSwitchingCompliances_ObjectIdentity=ObjectIdentity
efpSwitchingCompliances=_EfpSwitchingCompliances_ObjectIdentity((1,3,6,1,4,1,35265,1,103,5,3,1))
mibBuilder.exportSymbols(_B,**{'eltFastpathSwitchingMIB':eltFastpathSwitchingMIB,'efpSwitchingObjects':efpSwitchingObjects,'efpSwitchingCpuTrafficGlobals':efpSwitchingCpuTrafficGlobals,'efpSwitchingCpuTrafficConfigs':efpSwitchingCpuTrafficConfigs,'efpAgentCpuTrafficRateLimitQueueTable':efpAgentCpuTrafficRateLimitQueueTable,'efpAgentCpuTrafficRateLimitQueueEntry':efpAgentCpuTrafficRateLimitQueueEntry,_C:efpAgentCpuTrafficRateLimitQueueNumber,'efpAgentCpuTrafficRateLimitQueueLimit':efpAgentCpuTrafficRateLimitQueueLimit,'efpSwitchingCpuTrafficStatistics':efpSwitchingCpuTrafficStatistics,'efpAgentCpuTrafficRateLimitQueueStatTable':efpAgentCpuTrafficRateLimitQueueStatTable,'efpAgentCpuTrafficRateLimitQueueStatEntry':efpAgentCpuTrafficRateLimitQueueStatEntry,'efpAgentCpuTrafficRateLimitQueueRate':efpAgentCpuTrafficRateLimitQueueRate,'efpAgentCpuTrafficRateLimitQueuePackets':efpAgentCpuTrafficRateLimitQueuePackets,'efpSwitchingNotifications':efpSwitchingNotifications,'efpSwitchingNotificationsPrefix':efpSwitchingNotificationsPrefix,'efpSwitchingConformance':efpSwitchingConformance,'efpSwitchingCompliances':efpSwitchingCompliances})