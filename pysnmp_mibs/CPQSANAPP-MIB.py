_K='NotificationType'
_J='Integer32'
_I='swSequence'
_H='swFailure'
_G='swEventName'
_F='swSystemType'
_E='swSystemName'
_D='DisplayString'
_C='mandatory'
_B='read-write'
_A='CPQSANAPP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqSanAppliance_ObjectIdentity=ObjectIdentity
cpqSanAppliance=_CpqSanAppliance_ObjectIdentity((1,3,6,1,4,1,232,151))
_ResourceMonitor_ObjectIdentity=ObjectIdentity
resourceMonitor=_ResourceMonitor_ObjectIdentity((1,3,6,1,4,1,232,151,11))
class _SwSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_SwSystemName_Type.__name__=_D
_SwSystemName_Object=MibScalar
swSystemName=_SwSystemName_Object((1,3,6,1,4,1,232,151,11,1),_SwSystemName_Type())
swSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:swSystemName.setStatus(_C)
class _SwSystemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hsg80',1),('switch',2),('appliance',3)))
_SwSystemType_Type.__name__=_J
_SwSystemType_Object=MibScalar
swSystemType=_SwSystemType_Object((1,3,6,1,4,1,232,151,11,2),_SwSystemType_Type())
swSystemType.setMaxAccess(_B)
if mibBuilder.loadTexts:swSystemType.setStatus(_C)
class _SwEventName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_SwEventName_Type.__name__=_D
_SwEventName_Object=MibScalar
swEventName=_SwEventName_Object((1,3,6,1,4,1,232,151,11,3),_SwEventName_Type())
swEventName.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventName.setStatus(_C)
class _SwFailure_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_SwFailure_Type.__name__=_D
_SwFailure_Object=MibScalar
swFailure=_SwFailure_Object((1,3,6,1,4,1,232,151,11,4),_SwFailure_Type())
swFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:swFailure.setStatus(_C)
_SwSequence_Type=Integer32
_SwSequence_Object=MibScalar
swSequence=_SwSequence_Object((1,3,6,1,4,1,232,151,11,5),_SwSequence_Type())
swSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:swSequence.setStatus(_C)
swFailureTrap=NotificationType((1,3,6,1,4,1,232,151,11,0,1))
swFailureTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:swFailureTrap.setStatus('')
swWarningTrap=NotificationType((1,3,6,1,4,1,232,151,11,0,2))
swWarningTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:swWarningTrap.setStatus('')
swInformationTrap=NotificationType((1,3,6,1,4,1,232,151,11,0,4))
swInformationTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:swInformationTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'compaq':compaq,'cpqSanAppliance':cpqSanAppliance,'resourceMonitor':resourceMonitor,'swFailureTrap':swFailureTrap,'swWarningTrap':swWarningTrap,'swInformationTrap':swInformationTrap,_E:swSystemName,_F:swSystemType,_G:swEventName,_H:swFailure,_I:swSequence})