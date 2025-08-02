_I='arubaWiredInterfaceConfig'
_H='arubaWiredInterfaceSpeeds'
_G='arubaWiredInterfaceDuplex'
_F='arubaWiredInterfaceAutoneg'
_E='arubaWiredInterfaceIndex'
_D='read-write'
_C='Integer32'
_B='ARUBAWIRED-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arubaWiredInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,24))
if mibBuilder.loadTexts:arubaWiredInterfaceMIB.setRevisions(('2021-11-23 00:00',))
_ArubaWiredInterfaceSettings_ObjectIdentity=ObjectIdentity
arubaWiredInterfaceSettings=_ArubaWiredInterfaceSettings_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,24,1))
_ArubaWiredInterfaceTable_Object=MibTable
arubaWiredInterfaceTable=_ArubaWiredInterfaceTable_Object((1,3,6,1,4,1,47196,4,1,1,3,24,1,1))
if mibBuilder.loadTexts:arubaWiredInterfaceTable.setStatus(_A)
_ArubaWiredInterfaceEntry_Object=MibTableRow
arubaWiredInterfaceEntry=_ArubaWiredInterfaceEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,24,1,1,1))
arubaWiredInterfaceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:arubaWiredInterfaceEntry.setStatus(_A)
_ArubaWiredInterfaceIndex_Type=InterfaceIndex
_ArubaWiredInterfaceIndex_Object=MibTableColumn
arubaWiredInterfaceIndex=_ArubaWiredInterfaceIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,24,1,1,1,1),_ArubaWiredInterfaceIndex_Type())
arubaWiredInterfaceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredInterfaceIndex.setStatus(_A)
class _ArubaWiredInterfaceAutoneg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_ArubaWiredInterfaceAutoneg_Type.__name__=_C
_ArubaWiredInterfaceAutoneg_Object=MibTableColumn
arubaWiredInterfaceAutoneg=_ArubaWiredInterfaceAutoneg_Object((1,3,6,1,4,1,47196,4,1,1,3,24,1,1,1,2),_ArubaWiredInterfaceAutoneg_Type())
arubaWiredInterfaceAutoneg.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredInterfaceAutoneg.setStatus(_A)
class _ArubaWiredInterfaceDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('half',2)))
_ArubaWiredInterfaceDuplex_Type.__name__=_C
_ArubaWiredInterfaceDuplex_Object=MibTableColumn
arubaWiredInterfaceDuplex=_ArubaWiredInterfaceDuplex_Object((1,3,6,1,4,1,47196,4,1,1,3,24,1,1,1,3),_ArubaWiredInterfaceDuplex_Type())
arubaWiredInterfaceDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredInterfaceDuplex.setStatus(_A)
class _ArubaWiredInterfaceSpeeds_Type(Bits):namedValues=NamedValues(*(('speed10M',0),('speed100M',1),('speed1G',2),('speed2p5G',3),('speed5G',4),('speed10G',5),('speed25G',6),('speed40G',7),('speed50G',8),('speed100G',9),('speed200G',10),('speed400G',11),('speed800G',12)))
_ArubaWiredInterfaceSpeeds_Type.__name__='Bits'
_ArubaWiredInterfaceSpeeds_Object=MibTableColumn
arubaWiredInterfaceSpeeds=_ArubaWiredInterfaceSpeeds_Object((1,3,6,1,4,1,47196,4,1,1,3,24,1,1,1,4),_ArubaWiredInterfaceSpeeds_Type())
arubaWiredInterfaceSpeeds.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredInterfaceSpeeds.setStatus(_A)
_ArubaWiredInterfaceConformance_ObjectIdentity=ObjectIdentity
arubaWiredInterfaceConformance=_ArubaWiredInterfaceConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,24,2))
_ArubaWiredInterfaceGroups_ObjectIdentity=ObjectIdentity
arubaWiredInterfaceGroups=_ArubaWiredInterfaceGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,24,2,1))
_ArubaWiredInterfaceCompliances_ObjectIdentity=ObjectIdentity
arubaWiredInterfaceCompliances=_ArubaWiredInterfaceCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,24,2,2))
arubaWiredInterfaceConfig=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,24,2,1,1))
arubaWiredInterfaceConfig.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:arubaWiredInterfaceConfig.setStatus(_A)
arubaWiredInterfaceCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,24,2,2,1))
arubaWiredInterfaceCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:arubaWiredInterfaceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredInterfaceMIB':arubaWiredInterfaceMIB,'arubaWiredInterfaceSettings':arubaWiredInterfaceSettings,'arubaWiredInterfaceTable':arubaWiredInterfaceTable,'arubaWiredInterfaceEntry':arubaWiredInterfaceEntry,_E:arubaWiredInterfaceIndex,_F:arubaWiredInterfaceAutoneg,_G:arubaWiredInterfaceDuplex,_H:arubaWiredInterfaceSpeeds,'arubaWiredInterfaceConformance':arubaWiredInterfaceConformance,'arubaWiredInterfaceGroups':arubaWiredInterfaceGroups,_I:arubaWiredInterfaceConfig,'arubaWiredInterfaceCompliances':arubaWiredInterfaceCompliances,'arubaWiredInterfaceCompliance':arubaWiredInterfaceCompliance})