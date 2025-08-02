_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanInterfaces,ntEnterpriseDataTasmanMgmt,ntEnterpriseDataTasmanModules=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanInterfaces','ntEnterpriseDataTasmanMgmt','ntEnterpriseDataTasmanModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nndsxTC=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,3,2))
if mibBuilder.loadTexts:nndsxTC.setRevisions(('1999-04-23 00:00',))
class AlarmStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
class LEDState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('led-off',1),('led-green',2),('led-red',3),('led-yellow',4),('led-blinking-green',5),('led-blinking-red',6),('led-blinking-yellow',7)))
_NndsxMIB_ObjectIdentity=ObjectIdentity
nndsxMIB=_NndsxMIB_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1))
_NndsxT1E1IfGroup_ObjectIdentity=ObjectIdentity
nndsxT1E1IfGroup=_NndsxT1E1IfGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,2))
_NndsxT3E3IfGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfGroup=_NndsxT3E3IfGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3))
mibBuilder.exportSymbols('DSX-TC-MIB',**{'AlarmStatus':AlarmStatus,'LEDState':LEDState,'nndsxMIB':nndsxMIB,'nndsxT1E1IfGroup':nndsxT1E1IfGroup,'nndsxT3E3IfGroup':nndsxT3E3IfGroup,'nndsxTC':nndsxTC})