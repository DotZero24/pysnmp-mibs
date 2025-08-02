_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hcPerfHistTCMIB=ModuleIdentity((1,3,6,1,2,1,107))
if mibBuilder.loadTexts:hcPerfHistTCMIB.setRevisions(('2004-02-03 00:00',))
class HCPerfValidIntervals(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
class HCPerfInvalidIntervals(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
class HCPerfTimeElapsed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
class HCPerfIntervalThreshold(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
class HCPerfCurrentCount(TextualConvention,Counter64):status=_A
class HCPerfIntervalCount(TextualConvention,Counter64):status=_A
class HCPerfTotalCount(TextualConvention,Counter64):status=_A
mibBuilder.exportSymbols('HC-PerfHist-TC-MIB',**{'HCPerfValidIntervals':HCPerfValidIntervals,'HCPerfInvalidIntervals':HCPerfInvalidIntervals,'HCPerfTimeElapsed':HCPerfTimeElapsed,'HCPerfIntervalThreshold':HCPerfIntervalThreshold,'HCPerfCurrentCount':HCPerfCurrentCount,'HCPerfIntervalCount':HCPerfIntervalCount,'HCPerfTotalCount':HCPerfTotalCount,'hcPerfHistTCMIB':hcPerfHistTCMIB})