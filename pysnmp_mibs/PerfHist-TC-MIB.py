_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
perfHistTCMIB=ModuleIdentity((1,3,6,1,2,1,58))
if mibBuilder.loadTexts:perfHistTCMIB.setRevisions(('2003-08-13 00:00','1998-11-07 11:00'))
class PerfCurrentCount(TextualConvention,Gauge32):status=_A
class PerfIntervalCount(TextualConvention,Gauge32):status=_A
class PerfTotalCount(TextualConvention,Gauge32):status=_A
mibBuilder.exportSymbols('PerfHist-TC-MIB',**{'PerfCurrentCount':PerfCurrentCount,'PerfIntervalCount':PerfIntervalCount,'PerfTotalCount':PerfTotalCount,'perfHistTCMIB':perfHistTCMIB})