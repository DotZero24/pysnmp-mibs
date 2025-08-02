_F='trpzQosConfQosProfileConfigGroup'
_E='trpzQosConfQosProfConfMaxBandwidthKbps'
_D='trpzQosConfQosProfConfProfileName'
_C='OctetString'
_B='TRAPEZE-NETWORKS-QOS-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzQosConfigMib=ModuleIdentity((1,3,6,1,4,1,14525,4,20))
if mibBuilder.loadTexts:trpzQosConfigMib.setRevisions(('2011-02-24 00:11',))
_TrpzQosConfigMibObjects_ObjectIdentity=ObjectIdentity
trpzQosConfigMibObjects=_TrpzQosConfigMibObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,20,1))
_TrpzQosConfQosProfileConfigTable_Object=MibTable
trpzQosConfQosProfileConfigTable=_TrpzQosConfQosProfileConfigTable_Object((1,3,6,1,4,1,14525,4,20,1,1))
if mibBuilder.loadTexts:trpzQosConfQosProfileConfigTable.setStatus(_A)
_TrpzQosConfQosProfileConfigEntry_Object=MibTableRow
trpzQosConfQosProfileConfigEntry=_TrpzQosConfQosProfileConfigEntry_Object((1,3,6,1,4,1,14525,4,20,1,1,1))
trpzQosConfQosProfileConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:trpzQosConfQosProfileConfigEntry.setStatus(_A)
class _TrpzQosConfQosProfConfProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TrpzQosConfQosProfConfProfileName_Type.__name__=_C
_TrpzQosConfQosProfConfProfileName_Object=MibTableColumn
trpzQosConfQosProfConfProfileName=_TrpzQosConfQosProfConfProfileName_Object((1,3,6,1,4,1,14525,4,20,1,1,1,1),_TrpzQosConfQosProfConfProfileName_Type())
trpzQosConfQosProfConfProfileName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzQosConfQosProfConfProfileName.setStatus(_A)
_TrpzQosConfQosProfConfMaxBandwidthKbps_Type=Unsigned32
_TrpzQosConfQosProfConfMaxBandwidthKbps_Object=MibTableColumn
trpzQosConfQosProfConfMaxBandwidthKbps=_TrpzQosConfQosProfConfMaxBandwidthKbps_Object((1,3,6,1,4,1,14525,4,20,1,1,1,2),_TrpzQosConfQosProfConfMaxBandwidthKbps_Type())
trpzQosConfQosProfConfMaxBandwidthKbps.setMaxAccess('read-write')
if mibBuilder.loadTexts:trpzQosConfQosProfConfMaxBandwidthKbps.setStatus(_A)
_TrpzQosConfigConformance_ObjectIdentity=ObjectIdentity
trpzQosConfigConformance=_TrpzQosConfigConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,20,2))
_TrpzQosConfigCompliances_ObjectIdentity=ObjectIdentity
trpzQosConfigCompliances=_TrpzQosConfigCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,20,2,1))
_TrpzQosConfigGroups_ObjectIdentity=ObjectIdentity
trpzQosConfigGroups=_TrpzQosConfigGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,20,2,2))
trpzQosConfQosProfileConfigGroup=ObjectGroup((1,3,6,1,4,1,14525,4,20,2,2,1))
trpzQosConfQosProfileConfigGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:trpzQosConfQosProfileConfigGroup.setStatus(_A)
trpzQosConfigCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,20,2,1,1))
trpzQosConfigCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:trpzQosConfigCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'trpzQosConfigMib':trpzQosConfigMib,'trpzQosConfigMibObjects':trpzQosConfigMibObjects,'trpzQosConfQosProfileConfigTable':trpzQosConfQosProfileConfigTable,'trpzQosConfQosProfileConfigEntry':trpzQosConfQosProfileConfigEntry,_D:trpzQosConfQosProfConfProfileName,_E:trpzQosConfQosProfConfMaxBandwidthKbps,'trpzQosConfigConformance':trpzQosConfigConformance,'trpzQosConfigCompliances':trpzQosConfigCompliances,'trpzQosConfigCompliance':trpzQosConfigCompliance,'trpzQosConfigGroups':trpzQosConfigGroups,_F:trpzQosConfQosProfileConfigGroup})