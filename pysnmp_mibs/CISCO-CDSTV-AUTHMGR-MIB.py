_P='ciscoCdstvAuthMgrMIBMainObjectGroup'
_O='cdstvAuthMgrEventIsAddress'
_N='cdstvAuthMgrEventIsAddressType'
_M='cdstvAuthMgrAddressType'
_L='cdstvAuthMgrDebugLevel'
_K='cdstvAuthMgrServerThreadPool'
_J='cdstvAuthMgrTraxisSoapInterface'
_I='cdstvAuthMgrEventIsPort'
_H='cdstvAuthMgrPort'
_G='cdstvAuthMgrAddress'
_F='Unsigned32'
_E='Integer32'
_D='InetPortNumber'
_C='read-write'
_B='CISCO-CDSTV-AUTHMGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoURLStringOrEmpty,=mibBuilder.importSymbols('CISCO-TC','CiscoURLStringOrEmpty')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCdstvAuthmgrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,751))
if mibBuilder.loadTexts:ciscoCdstvAuthmgrMIB.setRevisions(('2010-07-20 00:00',))
_CiscoCdstvAuthMgrMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCdstvAuthMgrMIBNotifs=_CiscoCdstvAuthMgrMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,751,0))
_CiscoCdstvAuthMgrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdstvAuthMgrMIBObjects=_CiscoCdstvAuthMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,751,1))
_CdstvAuthMgrAddressType_Type=InetAddressType
_CdstvAuthMgrAddressType_Object=MibScalar
cdstvAuthMgrAddressType=_CdstvAuthMgrAddressType_Object((1,3,6,1,4,1,9,9,751,1,1),_CdstvAuthMgrAddressType_Type())
cdstvAuthMgrAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrAddressType.setStatus(_A)
_CdstvAuthMgrAddress_Type=InetAddress
_CdstvAuthMgrAddress_Object=MibScalar
cdstvAuthMgrAddress=_CdstvAuthMgrAddress_Object((1,3,6,1,4,1,9,9,751,1,2),_CdstvAuthMgrAddress_Type())
cdstvAuthMgrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrAddress.setStatus(_A)
class _CdstvAuthMgrPort_Type(InetPortNumber):defaultValue=7792
_CdstvAuthMgrPort_Type.__name__=_D
_CdstvAuthMgrPort_Object=MibScalar
cdstvAuthMgrPort=_CdstvAuthMgrPort_Object((1,3,6,1,4,1,9,9,751,1,3),_CdstvAuthMgrPort_Type())
cdstvAuthMgrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrPort.setStatus(_A)
_CdstvAuthMgrEventIsAddressType_Type=InetAddressType
_CdstvAuthMgrEventIsAddressType_Object=MibScalar
cdstvAuthMgrEventIsAddressType=_CdstvAuthMgrEventIsAddressType_Object((1,3,6,1,4,1,9,9,751,1,4),_CdstvAuthMgrEventIsAddressType_Type())
cdstvAuthMgrEventIsAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrEventIsAddressType.setStatus(_A)
_CdstvAuthMgrEventIsAddress_Type=InetAddress
_CdstvAuthMgrEventIsAddress_Object=MibScalar
cdstvAuthMgrEventIsAddress=_CdstvAuthMgrEventIsAddress_Object((1,3,6,1,4,1,9,9,751,1,5),_CdstvAuthMgrEventIsAddress_Type())
cdstvAuthMgrEventIsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrEventIsAddress.setStatus(_A)
_CdstvAuthMgrEventIsPort_Type=InetPortNumber
_CdstvAuthMgrEventIsPort_Object=MibScalar
cdstvAuthMgrEventIsPort=_CdstvAuthMgrEventIsPort_Object((1,3,6,1,4,1,9,9,751,1,6),_CdstvAuthMgrEventIsPort_Type())
cdstvAuthMgrEventIsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrEventIsPort.setStatus(_A)
_CdstvAuthMgrTraxisSoapInterface_Type=CiscoURLStringOrEmpty
_CdstvAuthMgrTraxisSoapInterface_Object=MibScalar
cdstvAuthMgrTraxisSoapInterface=_CdstvAuthMgrTraxisSoapInterface_Object((1,3,6,1,4,1,9,9,751,1,7),_CdstvAuthMgrTraxisSoapInterface_Type())
cdstvAuthMgrTraxisSoapInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrTraxisSoapInterface.setStatus(_A)
class _CdstvAuthMgrServerThreadPool_Type(Unsigned32):defaultValue=5
_CdstvAuthMgrServerThreadPool_Type.__name__=_F
_CdstvAuthMgrServerThreadPool_Object=MibScalar
cdstvAuthMgrServerThreadPool=_CdstvAuthMgrServerThreadPool_Object((1,3,6,1,4,1,9,9,751,1,8),_CdstvAuthMgrServerThreadPool_Type())
cdstvAuthMgrServerThreadPool.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrServerThreadPool.setStatus(_A)
class _CdstvAuthMgrDebugLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('low',2),('high',3)))
_CdstvAuthMgrDebugLevel_Type.__name__=_E
_CdstvAuthMgrDebugLevel_Object=MibScalar
cdstvAuthMgrDebugLevel=_CdstvAuthMgrDebugLevel_Object((1,3,6,1,4,1,9,9,751,1,9),_CdstvAuthMgrDebugLevel_Type())
cdstvAuthMgrDebugLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvAuthMgrDebugLevel.setStatus(_A)
_CiscoCdstvAuthMgrMIBConform_ObjectIdentity=ObjectIdentity
ciscoCdstvAuthMgrMIBConform=_CiscoCdstvAuthMgrMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,751,2))
_CiscoCdstvAuthMgrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdstvAuthMgrMIBCompliances=_CiscoCdstvAuthMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,751,2,1))
_CiscoCdstvAuthMgrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdstvAuthMgrMIBGroups=_CiscoCdstvAuthMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,751,2,2))
ciscoCdstvAuthMgrMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,751,2,2,1))
ciscoCdstvAuthMgrMIBMainObjectGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoCdstvAuthMgrMIBMainObjectGroup.setStatus(_A)
ciscoCdstvAuthMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,751,2,1,1))
ciscoCdstvAuthMgrMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoCdstvAuthMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCdstvAuthmgrMIB':ciscoCdstvAuthmgrMIB,'ciscoCdstvAuthMgrMIBNotifs':ciscoCdstvAuthMgrMIBNotifs,'ciscoCdstvAuthMgrMIBObjects':ciscoCdstvAuthMgrMIBObjects,_M:cdstvAuthMgrAddressType,_G:cdstvAuthMgrAddress,_H:cdstvAuthMgrPort,_N:cdstvAuthMgrEventIsAddressType,_O:cdstvAuthMgrEventIsAddress,_I:cdstvAuthMgrEventIsPort,_J:cdstvAuthMgrTraxisSoapInterface,_K:cdstvAuthMgrServerThreadPool,_L:cdstvAuthMgrDebugLevel,'ciscoCdstvAuthMgrMIBConform':ciscoCdstvAuthMgrMIBConform,'ciscoCdstvAuthMgrMIBCompliances':ciscoCdstvAuthMgrMIBCompliances,'ciscoCdstvAuthMgrMIBCompliance':ciscoCdstvAuthMgrMIBCompliance,'ciscoCdstvAuthMgrMIBGroups':ciscoCdstvAuthMgrMIBGroups,_P:ciscoCdstvAuthMgrMIBMainObjectGroup})