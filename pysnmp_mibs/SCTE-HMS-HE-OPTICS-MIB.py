_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
heOptics,=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','heOptics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heOpticsMib=ModuleIdentity((1,3,6,1,4,1,5591,1,11,1,0))
_HeOpticalTransmitterGroup_ObjectIdentity=ObjectIdentity
heOpticalTransmitterGroup=_HeOpticalTransmitterGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,1))
if mibBuilder.loadTexts:heOpticalTransmitterGroup.setStatus(_A)
_HeOpticalReceiverGroup_ObjectIdentity=ObjectIdentity
heOpticalReceiverGroup=_HeOpticalReceiverGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,2))
if mibBuilder.loadTexts:heOpticalReceiverGroup.setStatus(_A)
_HeOpticalAmplifierGroup_ObjectIdentity=ObjectIdentity
heOpticalAmplifierGroup=_HeOpticalAmplifierGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,3))
if mibBuilder.loadTexts:heOpticalAmplifierGroup.setStatus(_A)
_HeOpticalSwitchGroup_ObjectIdentity=ObjectIdentity
heOpticalSwitchGroup=_HeOpticalSwitchGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,4))
if mibBuilder.loadTexts:heOpticalSwitchGroup.setStatus(_A)
mibBuilder.exportSymbols('SCTE-HMS-HE-OPTICS-MIB',**{'heOpticsMib':heOpticsMib,'heOpticalTransmitterGroup':heOpticalTransmitterGroup,'heOpticalReceiverGroup':heOpticalReceiverGroup,'heOpticalAmplifierGroup':heOpticalAmplifierGroup,'heOpticalSwitchGroup':heOpticalSwitchGroup})