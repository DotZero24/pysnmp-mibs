_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
smartoptics,=mibBuilder.importSymbols('SO-MIB','smartoptics')
soTcMIB=ModuleIdentity((1,3,6,1,4,1,30826,3))
if mibBuilder.loadTexts:soTcMIB.setRevisions(('2022-09-05 14:10','2022-03-18 13:49','2021-04-12 10:49','2018-10-08 14:44'))
class OpticalPower1Decimal(TextualConvention,Integer32):status=_A;displayHint='d-1'
class DcpTenths(TextualConvention,Integer32):status=_A;displayHint='d-1'
class DcpHundreds(TextualConvention,Integer32):status=_A;displayHint='d-2'
class InterfaceStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('down',2),('up',3)))
class ItuPerceivedSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6)))
class OchPortMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),('off',2),('edfa',3),('express',4)))
class InterfacePortMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('na',1),('localAD',2),('xc1',3),('xc2',4),('xc3',5),('xc4Wss1',6),('xc4Wss2',7),('xc4Wss3',8),('xc4Wss4',9),('xc4Wss5',10)))
class FanStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPresent',1),('ok',2),('alarm',3)))
class FanMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('na',1),('high',2),('medium',3),('low',4)))
mibBuilder.exportSymbols('SO-TC-MIB',**{'OpticalPower1Decimal':OpticalPower1Decimal,'DcpTenths':DcpTenths,'DcpHundreds':DcpHundreds,'InterfaceStatus':InterfaceStatus,'ItuPerceivedSeverity':ItuPerceivedSeverity,'OchPortMode':OchPortMode,'InterfacePortMode':InterfacePortMode,'FanStatus':FanStatus,'FanMode':FanMode,'soTcMIB':soTcMIB})