_H='trpzPortConfigGroup'
_G='trpzPortConfigTrunkMaster'
_F='trpzPortConfigPoeMode'
_E='trpzPortConfigPortMode'
_D='trpzPortConfigPortNumber'
_C='read-only'
_B='TRAPEZE-NETWORKS-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
TrpzPhysPortNumber,TrpzPhysPortNumberOrZero=mibBuilder.importSymbols('TRAPEZE-NETWORKS-BASIC-TC','TrpzPhysPortNumber','TrpzPhysPortNumberOrZero')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzPortMib=ModuleIdentity((1,3,6,1,4,1,14525,4,6))
if mibBuilder.loadTexts:trpzPortMib.setRevisions(('2008-10-23 00:10','2008-05-19 00:04','2006-11-09 00:01','2006-04-06 00:00'))
class TrpzPortMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('directAttachAP',1),('networkPort',2),('wired',3)))
class TrpzPortPoeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('poeEnable',1),('poeDisable',2)))
_TrpzPortObjects_ObjectIdentity=ObjectIdentity
trpzPortObjects=_TrpzPortObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,6,1))
_TrpzPortDataObjects_ObjectIdentity=ObjectIdentity
trpzPortDataObjects=_TrpzPortDataObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,6,1,1))
_TrpzPortConfigTable_Object=MibTable
trpzPortConfigTable=_TrpzPortConfigTable_Object((1,3,6,1,4,1,14525,4,6,1,1,1))
if mibBuilder.loadTexts:trpzPortConfigTable.setStatus(_A)
_TrpzPortConfigEntry_Object=MibTableRow
trpzPortConfigEntry=_TrpzPortConfigEntry_Object((1,3,6,1,4,1,14525,4,6,1,1,1,1))
trpzPortConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:trpzPortConfigEntry.setStatus(_A)
_TrpzPortConfigPortNumber_Type=TrpzPhysPortNumber
_TrpzPortConfigPortNumber_Object=MibTableColumn
trpzPortConfigPortNumber=_TrpzPortConfigPortNumber_Object((1,3,6,1,4,1,14525,4,6,1,1,1,1,1),_TrpzPortConfigPortNumber_Type())
trpzPortConfigPortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzPortConfigPortNumber.setStatus(_A)
_TrpzPortConfigPortMode_Type=TrpzPortMode
_TrpzPortConfigPortMode_Object=MibTableColumn
trpzPortConfigPortMode=_TrpzPortConfigPortMode_Object((1,3,6,1,4,1,14525,4,6,1,1,1,1,2),_TrpzPortConfigPortMode_Type())
trpzPortConfigPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzPortConfigPortMode.setStatus(_A)
_TrpzPortConfigPoeMode_Type=TrpzPortPoeMode
_TrpzPortConfigPoeMode_Object=MibTableColumn
trpzPortConfigPoeMode=_TrpzPortConfigPoeMode_Object((1,3,6,1,4,1,14525,4,6,1,1,1,1,3),_TrpzPortConfigPoeMode_Type())
trpzPortConfigPoeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzPortConfigPoeMode.setStatus(_A)
_TrpzPortConfigTrunkMaster_Type=TrpzPhysPortNumberOrZero
_TrpzPortConfigTrunkMaster_Object=MibTableColumn
trpzPortConfigTrunkMaster=_TrpzPortConfigTrunkMaster_Object((1,3,6,1,4,1,14525,4,6,1,1,1,1,4),_TrpzPortConfigTrunkMaster_Type())
trpzPortConfigTrunkMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzPortConfigTrunkMaster.setStatus(_A)
_TrpzPortConformance_ObjectIdentity=ObjectIdentity
trpzPortConformance=_TrpzPortConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,6,1,2))
_TrpzPortCompliances_ObjectIdentity=ObjectIdentity
trpzPortCompliances=_TrpzPortCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,6,1,2,1))
_TrpzPortGroups_ObjectIdentity=ObjectIdentity
trpzPortGroups=_TrpzPortGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,6,1,2,2))
trpzPortConfigGroup=ObjectGroup((1,3,6,1,4,1,14525,4,6,1,2,2,1))
trpzPortConfigGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:trpzPortConfigGroup.setStatus(_A)
trpzPortCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,6,1,2,1,1))
trpzPortCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:trpzPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TrpzPortMode':TrpzPortMode,'TrpzPortPoeMode':TrpzPortPoeMode,'trpzPortMib':trpzPortMib,'trpzPortObjects':trpzPortObjects,'trpzPortDataObjects':trpzPortDataObjects,'trpzPortConfigTable':trpzPortConfigTable,'trpzPortConfigEntry':trpzPortConfigEntry,_D:trpzPortConfigPortNumber,_E:trpzPortConfigPortMode,_F:trpzPortConfigPoeMode,_G:trpzPortConfigTrunkMaster,'trpzPortConformance':trpzPortConformance,'trpzPortCompliances':trpzPortCompliances,'trpzPortCompliance':trpzPortCompliance,'trpzPortGroups':trpzPortGroups,_H:trpzPortConfigGroup})