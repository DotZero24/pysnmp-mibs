_F='cwmWirelessDeviceGroup'
_E='cwmTelnetLoginEnabled'
_D='cwmHttpServerEnabled'
_C='read-write'
_B='CISCO-WLAN-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoWlanManMIB=ModuleIdentity((1,3,6,1,4,1,9,9,415))
if mibBuilder.loadTexts:ciscoWlanManMIB.setRevisions(('2004-03-22 00:00',))
_CiscoWlanManMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWlanManMIBNotifs=_CiscoWlanManMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,415,0))
_CiscoWlanManMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWlanManMIBObjects=_CiscoWlanManMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,415,1))
_CwmDeviceConfig_ObjectIdentity=ObjectIdentity
cwmDeviceConfig=_CwmDeviceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,415,1,1))
_CwmHttpServerEnabled_Type=TruthValue
_CwmHttpServerEnabled_Object=MibScalar
cwmHttpServerEnabled=_CwmHttpServerEnabled_Object((1,3,6,1,4,1,9,9,415,1,1,1),_CwmHttpServerEnabled_Type())
cwmHttpServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmHttpServerEnabled.setStatus(_A)
_CwmTelnetLoginEnabled_Type=TruthValue
_CwmTelnetLoginEnabled_Object=MibScalar
cwmTelnetLoginEnabled=_CwmTelnetLoginEnabled_Object((1,3,6,1,4,1,9,9,415,1,1,2),_CwmTelnetLoginEnabled_Type())
cwmTelnetLoginEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmTelnetLoginEnabled.setStatus(_A)
_CwmNetworkConfig_ObjectIdentity=ObjectIdentity
cwmNetworkConfig=_CwmNetworkConfig_ObjectIdentity((1,3,6,1,4,1,9,9,415,1,2))
_CiscoWlanManMIBConform_ObjectIdentity=ObjectIdentity
ciscoWlanManMIBConform=_CiscoWlanManMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,415,2))
_CiscoWlanManMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWlanManMIBCompliances=_CiscoWlanManMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,415,2,1))
_CiscoWlanManMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWlanManMIBGroups=_CiscoWlanManMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,415,2,2))
cwmWirelessDeviceGroup=ObjectGroup((1,3,6,1,4,1,9,9,415,2,2,1))
cwmWirelessDeviceGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:cwmWirelessDeviceGroup.setStatus(_A)
ciscoWlanManMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,415,2,1,1))
ciscoWlanManMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoWlanManMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWlanManMIB':ciscoWlanManMIB,'ciscoWlanManMIBNotifs':ciscoWlanManMIBNotifs,'ciscoWlanManMIBObjects':ciscoWlanManMIBObjects,'cwmDeviceConfig':cwmDeviceConfig,_D:cwmHttpServerEnabled,_E:cwmTelnetLoginEnabled,'cwmNetworkConfig':cwmNetworkConfig,'ciscoWlanManMIBConform':ciscoWlanManMIBConform,'ciscoWlanManMIBCompliances':ciscoWlanManMIBCompliances,'ciscoWlanManMIBCompliance':ciscoWlanManMIBCompliance,'ciscoWlanManMIBGroups':ciscoWlanManMIBGroups,_F:cwmWirelessDeviceGroup})