_N='cIsnsServerConfigGroup'
_M='cIsnsClntServerProfileStatus'
_L='cIsnsClntServerProfilePort'
_K='cIsnsClntServerProfileAddr'
_J='cIsnsClntServerProfileAddrType'
_I='not-accessible'
_H='cIsnsClntServerIndex'
_G='cIsnsClntServerProfileName'
_F='Unsigned32'
_E='SnmpAdminString'
_D='CiscoPort'
_C='read-create'
_B='CISCO-ISNS-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,=mibBuilder.importSymbols('CISCO-TC',_D)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoIsnsClientMIB=ModuleIdentity((1,3,6,1,4,1,9,9,372))
if mibBuilder.loadTexts:ciscoIsnsClientMIB.setRevisions(('2003-11-10 00:00',))
_CiscoIsnsClientMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoIsnsClientMIBNotifications=_CiscoIsnsClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,372,0))
_CiscoIsnsClientMIBMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIsnsClientMIBMIBObjects=_CiscoIsnsClientMIBMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,372,1))
_CIsnsClientConfig_ObjectIdentity=ObjectIdentity
cIsnsClientConfig=_CIsnsClientConfig_ObjectIdentity((1,3,6,1,4,1,9,9,372,1,1))
_CIsnsClntServerProfileTable_Object=MibTable
cIsnsClntServerProfileTable=_CIsnsClntServerProfileTable_Object((1,3,6,1,4,1,9,9,372,1,1,1))
if mibBuilder.loadTexts:cIsnsClntServerProfileTable.setStatus(_A)
_CIsnsClntServerProfileEntry_Object=MibTableRow
cIsnsClntServerProfileEntry=_CIsnsClntServerProfileEntry_Object((1,3,6,1,4,1,9,9,372,1,1,1,1))
cIsnsClntServerProfileEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cIsnsClntServerProfileEntry.setStatus(_A)
class _CIsnsClntServerProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CIsnsClntServerProfileName_Type.__name__=_E
_CIsnsClntServerProfileName_Object=MibTableColumn
cIsnsClntServerProfileName=_CIsnsClntServerProfileName_Object((1,3,6,1,4,1,9,9,372,1,1,1,1,1),_CIsnsClntServerProfileName_Type())
cIsnsClntServerProfileName.setMaxAccess(_I)
if mibBuilder.loadTexts:cIsnsClntServerProfileName.setStatus(_A)
class _CIsnsClntServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CIsnsClntServerIndex_Type.__name__=_F
_CIsnsClntServerIndex_Object=MibTableColumn
cIsnsClntServerIndex=_CIsnsClntServerIndex_Object((1,3,6,1,4,1,9,9,372,1,1,1,1,2),_CIsnsClntServerIndex_Type())
cIsnsClntServerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cIsnsClntServerIndex.setStatus(_A)
_CIsnsClntServerProfileAddrType_Type=InetAddressType
_CIsnsClntServerProfileAddrType_Object=MibTableColumn
cIsnsClntServerProfileAddrType=_CIsnsClntServerProfileAddrType_Object((1,3,6,1,4,1,9,9,372,1,1,1,1,3),_CIsnsClntServerProfileAddrType_Type())
cIsnsClntServerProfileAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cIsnsClntServerProfileAddrType.setStatus(_A)
_CIsnsClntServerProfileAddr_Type=InetAddress
_CIsnsClntServerProfileAddr_Object=MibTableColumn
cIsnsClntServerProfileAddr=_CIsnsClntServerProfileAddr_Object((1,3,6,1,4,1,9,9,372,1,1,1,1,4),_CIsnsClntServerProfileAddr_Type())
cIsnsClntServerProfileAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cIsnsClntServerProfileAddr.setStatus(_A)
class _CIsnsClntServerProfilePort_Type(CiscoPort):defaultValue=3205
_CIsnsClntServerProfilePort_Type.__name__=_D
_CIsnsClntServerProfilePort_Object=MibTableColumn
cIsnsClntServerProfilePort=_CIsnsClntServerProfilePort_Object((1,3,6,1,4,1,9,9,372,1,1,1,1,5),_CIsnsClntServerProfilePort_Type())
cIsnsClntServerProfilePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cIsnsClntServerProfilePort.setStatus(_A)
_CIsnsClntServerProfileStatus_Type=RowStatus
_CIsnsClntServerProfileStatus_Object=MibTableColumn
cIsnsClntServerProfileStatus=_CIsnsClntServerProfileStatus_Object((1,3,6,1,4,1,9,9,372,1,1,1,1,6),_CIsnsClntServerProfileStatus_Type())
cIsnsClntServerProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cIsnsClntServerProfileStatus.setStatus(_A)
_CiscoIsnsClientMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIsnsClientMIBConformance=_CiscoIsnsClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,372,2))
_CiscoiIsnsClientMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoiIsnsClientMIBCompliances=_CiscoiIsnsClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,372,2,1))
_CiscoIsnsClientMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIsnsClientMIBGroups=_CiscoIsnsClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,372,2,2))
cIsnsServerConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,372,2,2,1))
cIsnsServerConfigGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cIsnsServerConfigGroup.setStatus(_A)
ciscoIsnsClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,372,2,1,1))
ciscoIsnsClientMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoIsnsClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIsnsClientMIB':ciscoIsnsClientMIB,'ciscoIsnsClientMIBNotifications':ciscoIsnsClientMIBNotifications,'ciscoIsnsClientMIBMIBObjects':ciscoIsnsClientMIBMIBObjects,'cIsnsClientConfig':cIsnsClientConfig,'cIsnsClntServerProfileTable':cIsnsClntServerProfileTable,'cIsnsClntServerProfileEntry':cIsnsClntServerProfileEntry,_G:cIsnsClntServerProfileName,_H:cIsnsClntServerIndex,_J:cIsnsClntServerProfileAddrType,_K:cIsnsClntServerProfileAddr,_L:cIsnsClntServerProfilePort,_M:cIsnsClntServerProfileStatus,'ciscoIsnsClientMIBConformance':ciscoIsnsClientMIBConformance,'ciscoiIsnsClientMIBCompliances':ciscoiIsnsClientMIBCompliances,'ciscoIsnsClientMIBCompliance':ciscoIsnsClientMIBCompliance,'ciscoIsnsClientMIBGroups':ciscoIsnsClientMIBGroups,_N:cIsnsServerConfigGroup})