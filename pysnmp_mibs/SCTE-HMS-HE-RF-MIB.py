_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
heRF,=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','heRF')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heRFMib=ModuleIdentity((1,3,6,1,4,1,5591,1,11,4,0))
_HeRFAmplifierGroup_ObjectIdentity=ObjectIdentity
heRFAmplifierGroup=_HeRFAmplifierGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,1))
if mibBuilder.loadTexts:heRFAmplifierGroup.setStatus(_A)
_HeRFSwitchGroup_ObjectIdentity=ObjectIdentity
heRFSwitchGroup=_HeRFSwitchGroup_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,2))
if mibBuilder.loadTexts:heRFSwitchGroup.setStatus(_A)
mibBuilder.exportSymbols('SCTE-HMS-HE-RF-MIB',**{'heRFMib':heRFMib,'heRFAmplifierGroup':heRFAmplifierGroup,'heRFSwitchGroup':heRFSwitchGroup})