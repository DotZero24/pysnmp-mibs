_F='raslogandSnmp'
_E='raslog'
_D='seconds'
_C='current'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
sw,=mibBuilder.importSymbols('SWBASE-MIB','sw')
swCpuOrMemoryUsage=ModuleIdentity((1,3,6,1,4,1,1588,2,1,1,1,26))
if mibBuilder.loadTexts:swCpuOrMemoryUsage.setRevisions(('1911-04-15 18:30','1913-06-05 11:30'))
class _SwCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwCpuUsage_Type.__name__=_A
_SwCpuUsage_Object=MibScalar
swCpuUsage=_SwCpuUsage_Object((1,3,6,1,4,1,1588,2,1,1,1,26,1),_SwCpuUsage_Type())
swCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuUsage.setStatus(_C)
class _SwCpuNoOfRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwCpuNoOfRetries_Type.__name__=_A
_SwCpuNoOfRetries_Object=MibScalar
swCpuNoOfRetries=_SwCpuNoOfRetries_Object((1,3,6,1,4,1,1588,2,1,1,1,26,2),_SwCpuNoOfRetries_Type())
swCpuNoOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuNoOfRetries.setStatus(_C)
class _SwCpuUsageLimit_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwCpuUsageLimit_Type.__name__=_A
_SwCpuUsageLimit_Object=MibScalar
swCpuUsageLimit=_SwCpuUsageLimit_Object((1,3,6,1,4,1,1588,2,1,1,1,26,3),_SwCpuUsageLimit_Type())
swCpuUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuUsageLimit.setStatus(_C)
class _SwCpuPollingInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_SwCpuPollingInterval_Type.__name__=_A
_SwCpuPollingInterval_Object=MibScalar
swCpuPollingInterval=_SwCpuPollingInterval_Object((1,3,6,1,4,1,1588,2,1,1,1,26,4),_SwCpuPollingInterval_Type())
swCpuPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuPollingInterval.setStatus(_C)
if mibBuilder.loadTexts:swCpuPollingInterval.setUnits(_D)
class _SwCpuAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),(_E,1),('snmp',2),(_F,3)))
_SwCpuAction_Type.__name__=_A
_SwCpuAction_Object=MibScalar
swCpuAction=_SwCpuAction_Object((1,3,6,1,4,1,1588,2,1,1,1,26,5),_SwCpuAction_Type())
swCpuAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuAction.setStatus(_C)
_SwMemUsage_Type=Integer32
_SwMemUsage_Object=MibScalar
swMemUsage=_SwMemUsage_Object((1,3,6,1,4,1,1588,2,1,1,1,26,6),_SwMemUsage_Type())
swMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsage.setStatus(_C)
class _SwMemNoOfRetries_Type(Integer32):defaultValue=3
_SwMemNoOfRetries_Type.__name__=_A
_SwMemNoOfRetries_Object=MibScalar
swMemNoOfRetries=_SwMemNoOfRetries_Object((1,3,6,1,4,1,1588,2,1,1,1,26,7),_SwMemNoOfRetries_Type())
swMemNoOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemNoOfRetries.setStatus(_C)
class _SwMemUsageLimit_Type(Integer32):defaultValue=60
_SwMemUsageLimit_Type.__name__=_A
_SwMemUsageLimit_Object=MibScalar
swMemUsageLimit=_SwMemUsageLimit_Object((1,3,6,1,4,1,1588,2,1,1,1,26,8),_SwMemUsageLimit_Type())
swMemUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsageLimit.setStatus(_C)
class _SwMemPollingInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_SwMemPollingInterval_Type.__name__=_A
_SwMemPollingInterval_Object=MibScalar
swMemPollingInterval=_SwMemPollingInterval_Object((1,3,6,1,4,1,1588,2,1,1,1,26,9),_SwMemPollingInterval_Type())
swMemPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemPollingInterval.setStatus(_C)
if mibBuilder.loadTexts:swMemPollingInterval.setUnits(_D)
class _SwMemAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),(_E,1),('snmp',2),(_F,3)))
_SwMemAction_Type.__name__=_A
_SwMemAction_Object=MibScalar
swMemAction=_SwMemAction_Object((1,3,6,1,4,1,1588,2,1,1,1,26,10),_SwMemAction_Type())
swMemAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemAction.setStatus(_C)
mibBuilder.exportSymbols('RESOURCE-MIB',**{'swCpuOrMemoryUsage':swCpuOrMemoryUsage,'swCpuUsage':swCpuUsage,'swCpuNoOfRetries':swCpuNoOfRetries,'swCpuUsageLimit':swCpuUsageLimit,'swCpuPollingInterval':swCpuPollingInterval,'swCpuAction':swCpuAction,'swMemUsage':swMemUsage,'swMemNoOfRetries':swMemNoOfRetries,'swMemUsageLimit':swMemUsageLimit,'swMemPollingInterval':swMemPollingInterval,'swMemAction':swMemAction})