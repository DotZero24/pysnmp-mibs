_M='ciscoLecDataVccBaseMIBGroup'
_L='cLecDataDirectRemoteAtmAddress'
_K='cLecDataDirectLocalAtmAddress'
_J='read-only'
_I='lecIndex'
_H='LAN-EMULATION-CLIENT-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='atmVclVpi'
_D='atmVclVci'
_C='ATM-MIB'
_B='CISCO-LEC-DATA-VCC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclVci,atmVclVpi=mibBuilder.importSymbols(_C,_D,_E)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
AtmLaneAddress,lecIndex=mibBuilder.importSymbols(_H,'AtmLaneAddress',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoLecDataVccMIB=ModuleIdentity((1,3,6,1,4,1,9,9,69))
if mibBuilder.loadTexts:ciscoLecDataVccMIB.setRevisions(('1997-01-06 00:00',))
_CiscoLecDataVccMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLecDataVccMIBObjects=_CiscoLecDataVccMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,69,1))
_CLecDataDirectVcc_ObjectIdentity=ObjectIdentity
cLecDataDirectVcc=_CLecDataDirectVcc_ObjectIdentity((1,3,6,1,4,1,9,9,69,1,1))
_CLecDataDirectVccTable_Object=MibTable
cLecDataDirectVccTable=_CLecDataDirectVccTable_Object((1,3,6,1,4,1,9,9,69,1,1,1))
if mibBuilder.loadTexts:cLecDataDirectVccTable.setStatus(_A)
_CLecDataDirectVccEntry_Object=MibTableRow
cLecDataDirectVccEntry=_CLecDataDirectVccEntry_Object((1,3,6,1,4,1,9,9,69,1,1,1,1))
cLecDataDirectVccEntry.setIndexNames((0,_H,_I),(0,_F,_G),(0,_C,_E),(0,_C,_D))
if mibBuilder.loadTexts:cLecDataDirectVccEntry.setStatus(_A)
_CLecDataDirectLocalAtmAddress_Type=AtmLaneAddress
_CLecDataDirectLocalAtmAddress_Object=MibTableColumn
cLecDataDirectLocalAtmAddress=_CLecDataDirectLocalAtmAddress_Object((1,3,6,1,4,1,9,9,69,1,1,1,1,1),_CLecDataDirectLocalAtmAddress_Type())
cLecDataDirectLocalAtmAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:cLecDataDirectLocalAtmAddress.setStatus(_A)
_CLecDataDirectRemoteAtmAddress_Type=AtmLaneAddress
_CLecDataDirectRemoteAtmAddress_Object=MibTableColumn
cLecDataDirectRemoteAtmAddress=_CLecDataDirectRemoteAtmAddress_Object((1,3,6,1,4,1,9,9,69,1,1,1,1,2),_CLecDataDirectRemoteAtmAddress_Type())
cLecDataDirectRemoteAtmAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:cLecDataDirectRemoteAtmAddress.setStatus(_A)
_CiscoLecDataVccMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoLecDataVccMIBNotificationPrefix=_CiscoLecDataVccMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,69,2))
_CiscoLecDataVccMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoLecDataVccMIBNotifications=_CiscoLecDataVccMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,69,2,0))
_CiscoLecDataVccMIBConformance_ObjectIdentity=ObjectIdentity
ciscoLecDataVccMIBConformance=_CiscoLecDataVccMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,69,3))
_CiscoLecDataVccMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLecDataVccMIBCompliances=_CiscoLecDataVccMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,69,3,1))
_CiscoLecDataVccMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLecDataVccMIBGroups=_CiscoLecDataVccMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,69,3,2))
ciscoLecDataVccBaseMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,69,3,2,1))
ciscoLecDataVccBaseMIBGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoLecDataVccBaseMIBGroup.setStatus(_A)
ciscoLecDataVccMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,69,3,1,1))
ciscoLecDataVccMIBCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoLecDataVccMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLecDataVccMIB':ciscoLecDataVccMIB,'ciscoLecDataVccMIBObjects':ciscoLecDataVccMIBObjects,'cLecDataDirectVcc':cLecDataDirectVcc,'cLecDataDirectVccTable':cLecDataDirectVccTable,'cLecDataDirectVccEntry':cLecDataDirectVccEntry,_K:cLecDataDirectLocalAtmAddress,_L:cLecDataDirectRemoteAtmAddress,'ciscoLecDataVccMIBNotificationPrefix':ciscoLecDataVccMIBNotificationPrefix,'ciscoLecDataVccMIBNotifications':ciscoLecDataVccMIBNotifications,'ciscoLecDataVccMIBConformance':ciscoLecDataVccMIBConformance,'ciscoLecDataVccMIBCompliances':ciscoLecDataVccMIBCompliances,'ciscoLecDataVccMIBCompliance':ciscoLecDataVccMIBCompliance,'ciscoLecDataVccMIBGroups':ciscoLecDataVccMIBGroups,_M:ciscoLecDataVccBaseMIBGroup})