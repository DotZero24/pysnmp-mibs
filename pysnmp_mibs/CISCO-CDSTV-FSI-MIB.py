_N='ciscoCdstvFsiMIBMainObjectGroup'
_M='cdstvFsiIpAddressType'
_L='cdstvFsiAsyncCallbackURL'
_K='cdstvFsiContentRootPath'
_J='cdstvFsiLogLevel'
_I='cdstvFsiFtpOutLoginTTL'
_H='cdstvFsiFtpOutServerPort'
_G='cdstvFsiFtpClientPort'
_F='cdstvFsiServerPort'
_E='cdstvFsiIpAddress'
_D='Integer32'
_C='read-write'
_B='CISCO-CDSTV-FSI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoURLString,=mibBuilder.importSymbols('CISCO-TC','CiscoURLString')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCdstvFsiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,735))
if mibBuilder.loadTexts:ciscoCdstvFsiMIB.setRevisions(('2010-05-10 00:00',))
_CiscoCdstvFsiMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCdstvFsiMIBNotifs=_CiscoCdstvFsiMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,735,0))
_CiscoCdstvFsiMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdstvFsiMIBObjects=_CiscoCdstvFsiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,735,1))
_CdstvFsiIpAddressType_Type=InetAddressType
_CdstvFsiIpAddressType_Object=MibScalar
cdstvFsiIpAddressType=_CdstvFsiIpAddressType_Object((1,3,6,1,4,1,9,9,735,1,1),_CdstvFsiIpAddressType_Type())
cdstvFsiIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiIpAddressType.setStatus(_A)
_CdstvFsiIpAddress_Type=InetAddress
_CdstvFsiIpAddress_Object=MibScalar
cdstvFsiIpAddress=_CdstvFsiIpAddress_Object((1,3,6,1,4,1,9,9,735,1,2),_CdstvFsiIpAddress_Type())
cdstvFsiIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiIpAddress.setStatus(_A)
_CdstvFsiServerPort_Type=InetPortNumber
_CdstvFsiServerPort_Object=MibScalar
cdstvFsiServerPort=_CdstvFsiServerPort_Object((1,3,6,1,4,1,9,9,735,1,3),_CdstvFsiServerPort_Type())
cdstvFsiServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiServerPort.setStatus(_A)
_CdstvFsiFtpClientPort_Type=InetPortNumber
_CdstvFsiFtpClientPort_Object=MibScalar
cdstvFsiFtpClientPort=_CdstvFsiFtpClientPort_Object((1,3,6,1,4,1,9,9,735,1,4),_CdstvFsiFtpClientPort_Type())
cdstvFsiFtpClientPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiFtpClientPort.setStatus(_A)
_CdstvFsiFtpOutServerPort_Type=InetPortNumber
_CdstvFsiFtpOutServerPort_Object=MibScalar
cdstvFsiFtpOutServerPort=_CdstvFsiFtpOutServerPort_Object((1,3,6,1,4,1,9,9,735,1,5),_CdstvFsiFtpOutServerPort_Type())
cdstvFsiFtpOutServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiFtpOutServerPort.setStatus(_A)
_CdstvFsiFtpOutLoginTTL_Type=Unsigned32
_CdstvFsiFtpOutLoginTTL_Object=MibScalar
cdstvFsiFtpOutLoginTTL=_CdstvFsiFtpOutLoginTTL_Object((1,3,6,1,4,1,9,9,735,1,6),_CdstvFsiFtpOutLoginTTL_Type())
cdstvFsiFtpOutLoginTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiFtpOutLoginTTL.setStatus(_A)
if mibBuilder.loadTexts:cdstvFsiFtpOutLoginTTL.setUnits('hops')
class _CdstvFsiLogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('low',2),('high',3)))
_CdstvFsiLogLevel_Type.__name__=_D
_CdstvFsiLogLevel_Object=MibScalar
cdstvFsiLogLevel=_CdstvFsiLogLevel_Object((1,3,6,1,4,1,9,9,735,1,7),_CdstvFsiLogLevel_Type())
cdstvFsiLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiLogLevel.setStatus(_A)
_CdstvFsiContentRootPath_Type=SnmpAdminString
_CdstvFsiContentRootPath_Object=MibScalar
cdstvFsiContentRootPath=_CdstvFsiContentRootPath_Object((1,3,6,1,4,1,9,9,735,1,8),_CdstvFsiContentRootPath_Type())
cdstvFsiContentRootPath.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiContentRootPath.setStatus(_A)
_CdstvFsiAsyncCallbackURL_Type=CiscoURLString
_CdstvFsiAsyncCallbackURL_Object=MibScalar
cdstvFsiAsyncCallbackURL=_CdstvFsiAsyncCallbackURL_Object((1,3,6,1,4,1,9,9,735,1,9),_CdstvFsiAsyncCallbackURL_Type())
cdstvFsiAsyncCallbackURL.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvFsiAsyncCallbackURL.setStatus(_A)
_CiscoCdstvFsiMIBConform_ObjectIdentity=ObjectIdentity
ciscoCdstvFsiMIBConform=_CiscoCdstvFsiMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,735,2))
_CiscoCdstvFsiMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdstvFsiMIBCompliances=_CiscoCdstvFsiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,735,2,1))
_CiscoCdstvFsiMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdstvFsiMIBGroups=_CiscoCdstvFsiMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,735,2,2))
ciscoCdstvFsiMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,735,2,2,1))
ciscoCdstvFsiMIBMainObjectGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoCdstvFsiMIBMainObjectGroup.setStatus(_A)
ciscoCdstvFsiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,735,2,1,1))
ciscoCdstvFsiMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoCdstvFsiMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCdstvFsiMIB':ciscoCdstvFsiMIB,'ciscoCdstvFsiMIBNotifs':ciscoCdstvFsiMIBNotifs,'ciscoCdstvFsiMIBObjects':ciscoCdstvFsiMIBObjects,_M:cdstvFsiIpAddressType,_E:cdstvFsiIpAddress,_F:cdstvFsiServerPort,_G:cdstvFsiFtpClientPort,_H:cdstvFsiFtpOutServerPort,_I:cdstvFsiFtpOutLoginTTL,_J:cdstvFsiLogLevel,_K:cdstvFsiContentRootPath,_L:cdstvFsiAsyncCallbackURL,'ciscoCdstvFsiMIBConform':ciscoCdstvFsiMIBConform,'ciscoCdstvFsiMIBCompliances':ciscoCdstvFsiMIBCompliances,'ciscoCdstvFsiMIBCompliance':ciscoCdstvFsiMIBCompliance,'ciscoCdstvFsiMIBGroups':ciscoCdstvFsiMIBGroups,_N:ciscoCdstvFsiMIBMainObjectGroup})