_H='ntwsPortConfigGroup'
_G='ntwsPortConfigTrunkMaster'
_F='ntwsPortConfigPoeMode'
_E='ntwsPortConfigPortMode'
_D='ntwsPortConfigPortNumber'
_C='read-only'
_B='NTWS-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsPhysPortNumber,NtwsPhysPortNumberOrZero=mibBuilder.importSymbols('NTWS-BASIC-TC','NtwsPhysPortNumber','NtwsPhysPortNumberOrZero')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntwsPortMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,6))
if mibBuilder.loadTexts:ntwsPortMib.setRevisions(('2008-10-23 00:10','2008-05-19 00:04','2007-08-16 00:02','2006-11-09 00:01','2006-04-06 00:00'))
class NtwsPortMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('directAttachAP',1),('networkPort',2),('wired',3)))
class NtwsPortPoeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('poeEnable',1),('poeDisable',2)))
_NtwsPortObjects_ObjectIdentity=ObjectIdentity
ntwsPortObjects=_NtwsPortObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,6,1))
_NtwsPortDataObjects_ObjectIdentity=ObjectIdentity
ntwsPortDataObjects=_NtwsPortDataObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,6,1,1))
_NtwsPortConfigTable_Object=MibTable
ntwsPortConfigTable=_NtwsPortConfigTable_Object((1,3,6,1,4,1,45,6,1,4,6,1,1,1))
if mibBuilder.loadTexts:ntwsPortConfigTable.setStatus(_A)
_NtwsPortConfigEntry_Object=MibTableRow
ntwsPortConfigEntry=_NtwsPortConfigEntry_Object((1,3,6,1,4,1,45,6,1,4,6,1,1,1,1))
ntwsPortConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ntwsPortConfigEntry.setStatus(_A)
_NtwsPortConfigPortNumber_Type=NtwsPhysPortNumber
_NtwsPortConfigPortNumber_Object=MibTableColumn
ntwsPortConfigPortNumber=_NtwsPortConfigPortNumber_Object((1,3,6,1,4,1,45,6,1,4,6,1,1,1,1,1),_NtwsPortConfigPortNumber_Type())
ntwsPortConfigPortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntwsPortConfigPortNumber.setStatus(_A)
_NtwsPortConfigPortMode_Type=NtwsPortMode
_NtwsPortConfigPortMode_Object=MibTableColumn
ntwsPortConfigPortMode=_NtwsPortConfigPortMode_Object((1,3,6,1,4,1,45,6,1,4,6,1,1,1,1,2),_NtwsPortConfigPortMode_Type())
ntwsPortConfigPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsPortConfigPortMode.setStatus(_A)
_NtwsPortConfigPoeMode_Type=NtwsPortPoeMode
_NtwsPortConfigPoeMode_Object=MibTableColumn
ntwsPortConfigPoeMode=_NtwsPortConfigPoeMode_Object((1,3,6,1,4,1,45,6,1,4,6,1,1,1,1,3),_NtwsPortConfigPoeMode_Type())
ntwsPortConfigPoeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsPortConfigPoeMode.setStatus(_A)
_NtwsPortConfigTrunkMaster_Type=NtwsPhysPortNumberOrZero
_NtwsPortConfigTrunkMaster_Object=MibTableColumn
ntwsPortConfigTrunkMaster=_NtwsPortConfigTrunkMaster_Object((1,3,6,1,4,1,45,6,1,4,6,1,1,1,1,4),_NtwsPortConfigTrunkMaster_Type())
ntwsPortConfigTrunkMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsPortConfigTrunkMaster.setStatus(_A)
_NtwsPortConformance_ObjectIdentity=ObjectIdentity
ntwsPortConformance=_NtwsPortConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,6,1,2))
_NtwsPortCompliances_ObjectIdentity=ObjectIdentity
ntwsPortCompliances=_NtwsPortCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,6,1,2,1))
_NtwsPortGroups_ObjectIdentity=ObjectIdentity
ntwsPortGroups=_NtwsPortGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,6,1,2,2))
ntwsPortConfigGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,6,1,2,2,1))
ntwsPortConfigGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ntwsPortConfigGroup.setStatus(_A)
ntwsPortCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,6,1,2,1,1))
ntwsPortCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ntwsPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NtwsPortMode':NtwsPortMode,'NtwsPortPoeMode':NtwsPortPoeMode,'ntwsPortMib':ntwsPortMib,'ntwsPortObjects':ntwsPortObjects,'ntwsPortDataObjects':ntwsPortDataObjects,'ntwsPortConfigTable':ntwsPortConfigTable,'ntwsPortConfigEntry':ntwsPortConfigEntry,_D:ntwsPortConfigPortNumber,_E:ntwsPortConfigPortMode,_F:ntwsPortConfigPoeMode,_G:ntwsPortConfigTrunkMaster,'ntwsPortConformance':ntwsPortConformance,'ntwsPortCompliances':ntwsPortCompliances,'ntwsPortCompliance':ntwsPortCompliance,'ntwsPortGroups':ntwsPortGroups,_H:ntwsPortConfigGroup})