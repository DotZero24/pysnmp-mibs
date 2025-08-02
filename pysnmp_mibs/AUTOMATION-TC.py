_B='1a'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
automationModules,=mibBuilder.importSymbols('AUTOMATION-SMI','automationModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
automationTcModule=ModuleIdentity((1,3,6,1,4,1,4329,6,2,1))
if mibBuilder.loadTexts:automationTcModule.setRevisions(('2013-06-30 00:00','2012-09-19 00:00','2012-07-27 00:00','2008-11-10 00:00','2008-04-29 00:00','2005-01-12 00:00'))
class AutomationOrderNumberTC(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,32))
class AutomationSerialNumberTC(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
class AutomationVersionNumberTC(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class AutomationMacAddressTC(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class AutomationIpAddressTC(TextualConvention,OctetString):status=_A;displayHint=_B
class AutomationStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('invalid',0),('enable',1),('disable',2)))
class AutomationTriggerTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trigger',1),('notTriggered',2)))
class AutomationFunctionStringTC(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
class AutomationLocationStringTC(TextualConvention,OctetString):status=_A;displayHint='22a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(22,22));fixedLength=22
mibBuilder.exportSymbols('AUTOMATION-TC',**{'AutomationOrderNumberTC':AutomationOrderNumberTC,'AutomationSerialNumberTC':AutomationSerialNumberTC,'AutomationVersionNumberTC':AutomationVersionNumberTC,'AutomationMacAddressTC':AutomationMacAddressTC,'AutomationIpAddressTC':AutomationIpAddressTC,'AutomationStatusTC':AutomationStatusTC,'AutomationTriggerTC':AutomationTriggerTC,'AutomationFunctionStringTC':AutomationFunctionStringTC,'AutomationLocationStringTC':AutomationLocationStringTC,'automationTcModule':automationTcModule})