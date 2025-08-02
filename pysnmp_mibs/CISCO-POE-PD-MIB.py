_J='cpoePdInformationGroup'
_I='cpoePdSupportedPowerMode'
_H='cpoePdSupportedPower'
_G='cpoePdCurrentPowerSource'
_F='cpoePdCurrentPowerLevel'
_E='cpoePdSupportedPowerLevel'
_D='read-only'
_C='Unsigned32'
_B='CISCO-POE-PD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoPoePdMIB=ModuleIdentity((1,3,6,1,4,1,9,9,414))
if mibBuilder.loadTexts:ciscoPoePdMIB.setRevisions(('2004-05-05 00:00',))
class CpoePdPowerSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('pending',1),('acAdaptor',2),('thirdParty',3),('classic',4),('midspan',5),('cdpNegotiated',6),('highPowerClassic',7)))
_CpoePdMIBNotifications_ObjectIdentity=ObjectIdentity
cpoePdMIBNotifications=_CpoePdMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,414,0))
_CpoePdMIBObjects_ObjectIdentity=ObjectIdentity
cpoePdMIBObjects=_CpoePdMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,414,1))
_CpoePdInformation_ObjectIdentity=ObjectIdentity
cpoePdInformation=_CpoePdInformation_ObjectIdentity((1,3,6,1,4,1,9,9,414,1,1))
class _CpoePdCurrentPowerLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpoePdCurrentPowerLevel_Type.__name__=_C
_CpoePdCurrentPowerLevel_Object=MibScalar
cpoePdCurrentPowerLevel=_CpoePdCurrentPowerLevel_Object((1,3,6,1,4,1,9,9,414,1,1,1),_CpoePdCurrentPowerLevel_Type())
cpoePdCurrentPowerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:cpoePdCurrentPowerLevel.setStatus(_A)
_CpoePdCurrentPowerSource_Type=CpoePdPowerSourceType
_CpoePdCurrentPowerSource_Object=MibScalar
cpoePdCurrentPowerSource=_CpoePdCurrentPowerSource_Object((1,3,6,1,4,1,9,9,414,1,1,2),_CpoePdCurrentPowerSource_Type())
cpoePdCurrentPowerSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cpoePdCurrentPowerSource.setStatus(_A)
_CpoePdSupportedPowerLevelTable_Object=MibTable
cpoePdSupportedPowerLevelTable=_CpoePdSupportedPowerLevelTable_Object((1,3,6,1,4,1,9,9,414,1,1,3))
if mibBuilder.loadTexts:cpoePdSupportedPowerLevelTable.setStatus(_A)
_CpoePdSupportedPowerLevelEntry_Object=MibTableRow
cpoePdSupportedPowerLevelEntry=_CpoePdSupportedPowerLevelEntry_Object((1,3,6,1,4,1,9,9,414,1,1,3,1))
cpoePdSupportedPowerLevelEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpoePdSupportedPowerLevelEntry.setStatus(_A)
class _CpoePdSupportedPowerLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpoePdSupportedPowerLevel_Type.__name__=_C
_CpoePdSupportedPowerLevel_Object=MibTableColumn
cpoePdSupportedPowerLevel=_CpoePdSupportedPowerLevel_Object((1,3,6,1,4,1,9,9,414,1,1,3,1,1),_CpoePdSupportedPowerLevel_Type())
cpoePdSupportedPowerLevel.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cpoePdSupportedPowerLevel.setStatus(_A)
class _CpoePdSupportedPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpoePdSupportedPower_Type.__name__=_C
_CpoePdSupportedPower_Object=MibTableColumn
cpoePdSupportedPower=_CpoePdSupportedPower_Object((1,3,6,1,4,1,9,9,414,1,1,3,1,2),_CpoePdSupportedPower_Type())
cpoePdSupportedPower.setMaxAccess(_D)
if mibBuilder.loadTexts:cpoePdSupportedPower.setStatus(_A)
if mibBuilder.loadTexts:cpoePdSupportedPower.setUnits('milliwatts')
_CpoePdSupportedPowerMode_Type=SnmpAdminString
_CpoePdSupportedPowerMode_Object=MibTableColumn
cpoePdSupportedPowerMode=_CpoePdSupportedPowerMode_Object((1,3,6,1,4,1,9,9,414,1,1,3,1,3),_CpoePdSupportedPowerMode_Type())
cpoePdSupportedPowerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cpoePdSupportedPowerMode.setStatus(_A)
_CpoePdMIBConformance_ObjectIdentity=ObjectIdentity
cpoePdMIBConformance=_CpoePdMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,414,2))
_CpoePdMIBCompliances_ObjectIdentity=ObjectIdentity
cpoePdMIBCompliances=_CpoePdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,414,2,1))
_CpoePdMIBGroups_ObjectIdentity=ObjectIdentity
cpoePdMIBGroups=_CpoePdMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,414,2,2))
cpoePdInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,414,2,2,1))
cpoePdInformationGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cpoePdInformationGroup.setStatus(_A)
cpoePdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,414,2,1,1))
cpoePdMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:cpoePdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CpoePdPowerSourceType':CpoePdPowerSourceType,'ciscoPoePdMIB':ciscoPoePdMIB,'cpoePdMIBNotifications':cpoePdMIBNotifications,'cpoePdMIBObjects':cpoePdMIBObjects,'cpoePdInformation':cpoePdInformation,_F:cpoePdCurrentPowerLevel,_G:cpoePdCurrentPowerSource,'cpoePdSupportedPowerLevelTable':cpoePdSupportedPowerLevelTable,'cpoePdSupportedPowerLevelEntry':cpoePdSupportedPowerLevelEntry,_E:cpoePdSupportedPowerLevel,_H:cpoePdSupportedPower,_I:cpoePdSupportedPowerMode,'cpoePdMIBConformance':cpoePdMIBConformance,'cpoePdMIBCompliances':cpoePdMIBCompliances,'cpoePdMIBCompliance':cpoePdMIBCompliance,'cpoePdMIBGroups':cpoePdMIBGroups,_J:cpoePdInformationGroup})