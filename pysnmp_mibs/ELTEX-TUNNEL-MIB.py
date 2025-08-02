_K='tunnelWiFiConfigID'
_J='tunnelWiFiConfigEncapsMethod'
_I='tunnelWiFiConfigRemoteAddress'
_H='tunnelWiFiConfigRemoteAddressType'
_G='tunnelWiFiConfigLocalAddress'
_F='tunnelWiFiConfigLocalAddressType'
_E='read-only'
_D='Integer32'
_C='not-accessible'
_B='ELTEX-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
IANAtunnelType,=mibBuilder.importSymbols('IANAifType-MIB','IANAtunnelType')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltexTunnelMIB=ModuleIdentity((1,3,6,1,4,1,35265,21))
if mibBuilder.loadTexts:eltexTunnelMIB.setRevisions(('2015-12-29 00:00',))
_TunnelWiFiConfigTable_Object=MibTable
tunnelWiFiConfigTable=_TunnelWiFiConfigTable_Object((1,3,6,1,4,1,35265,21,1))
if mibBuilder.loadTexts:tunnelWiFiConfigTable.setStatus(_A)
_TunnelWiFiConfigEntry_Object=MibTableRow
tunnelWiFiConfigEntry=_TunnelWiFiConfigEntry_Object((1,3,6,1,4,1,35265,21,1,1))
tunnelWiFiConfigEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:tunnelWiFiConfigEntry.setStatus(_A)
_TunnelWiFiConfigLocalAddressType_Type=InetAddressType
_TunnelWiFiConfigLocalAddressType_Object=MibTableColumn
tunnelWiFiConfigLocalAddressType=_TunnelWiFiConfigLocalAddressType_Object((1,3,6,1,4,1,35265,21,1,1,1),_TunnelWiFiConfigLocalAddressType_Type())
tunnelWiFiConfigLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelWiFiConfigLocalAddressType.setStatus(_A)
_TunnelWiFiConfigLocalAddress_Type=InetAddress
_TunnelWiFiConfigLocalAddress_Object=MibTableColumn
tunnelWiFiConfigLocalAddress=_TunnelWiFiConfigLocalAddress_Object((1,3,6,1,4,1,35265,21,1,1,2),_TunnelWiFiConfigLocalAddress_Type())
tunnelWiFiConfigLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelWiFiConfigLocalAddress.setStatus(_A)
_TunnelWiFiConfigRemoteAddressType_Type=InetAddressType
_TunnelWiFiConfigRemoteAddressType_Object=MibTableColumn
tunnelWiFiConfigRemoteAddressType=_TunnelWiFiConfigRemoteAddressType_Object((1,3,6,1,4,1,35265,21,1,1,3),_TunnelWiFiConfigRemoteAddressType_Type())
tunnelWiFiConfigRemoteAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelWiFiConfigRemoteAddressType.setStatus(_A)
_TunnelWiFiConfigRemoteAddress_Type=InetAddress
_TunnelWiFiConfigRemoteAddress_Object=MibTableColumn
tunnelWiFiConfigRemoteAddress=_TunnelWiFiConfigRemoteAddress_Object((1,3,6,1,4,1,35265,21,1,1,4),_TunnelWiFiConfigRemoteAddress_Type())
tunnelWiFiConfigRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelWiFiConfigRemoteAddress.setStatus(_A)
_TunnelWiFiConfigEncapsMethod_Type=IANAtunnelType
_TunnelWiFiConfigEncapsMethod_Object=MibTableColumn
tunnelWiFiConfigEncapsMethod=_TunnelWiFiConfigEncapsMethod_Object((1,3,6,1,4,1,35265,21,1,1,5),_TunnelWiFiConfigEncapsMethod_Type())
tunnelWiFiConfigEncapsMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelWiFiConfigEncapsMethod.setStatus(_A)
class _TunnelWiFiConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TunnelWiFiConfigID_Type.__name__=_D
_TunnelWiFiConfigID_Object=MibTableColumn
tunnelWiFiConfigID=_TunnelWiFiConfigID_Object((1,3,6,1,4,1,35265,21,1,1,6),_TunnelWiFiConfigID_Type())
tunnelWiFiConfigID.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelWiFiConfigID.setStatus(_A)
_TunnelWiFiConfigIfIndex_Type=InterfaceIndexOrZero
_TunnelWiFiConfigIfIndex_Object=MibTableColumn
tunnelWiFiConfigIfIndex=_TunnelWiFiConfigIfIndex_Object((1,3,6,1,4,1,35265,21,1,1,7),_TunnelWiFiConfigIfIndex_Type())
tunnelWiFiConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tunnelWiFiConfigIfIndex.setStatus(_A)
_TunnelWiFiConfigStatus_Type=RowStatus
_TunnelWiFiConfigStatus_Object=MibTableColumn
tunnelWiFiConfigStatus=_TunnelWiFiConfigStatus_Object((1,3,6,1,4,1,35265,21,1,1,8),_TunnelWiFiConfigStatus_Type())
tunnelWiFiConfigStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:tunnelWiFiConfigStatus.setStatus(_A)
class _TunnelWiFiConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notConfigured',0),('management',1),('data',2)))
_TunnelWiFiConfigMode_Type.__name__=_D
_TunnelWiFiConfigMode_Object=MibTableColumn
tunnelWiFiConfigMode=_TunnelWiFiConfigMode_Object((1,3,6,1,4,1,35265,21,1,1,9),_TunnelWiFiConfigMode_Type())
tunnelWiFiConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tunnelWiFiConfigMode.setStatus(_A)
_TunnelWiFiConfigDefaultProfile_Type=TruthValue
_TunnelWiFiConfigDefaultProfile_Object=MibTableColumn
tunnelWiFiConfigDefaultProfile=_TunnelWiFiConfigDefaultProfile_Object((1,3,6,1,4,1,35265,21,1,1,10),_TunnelWiFiConfigDefaultProfile_Type())
tunnelWiFiConfigDefaultProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:tunnelWiFiConfigDefaultProfile.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltexTunnelMIB':eltexTunnelMIB,'tunnelWiFiConfigTable':tunnelWiFiConfigTable,'tunnelWiFiConfigEntry':tunnelWiFiConfigEntry,_F:tunnelWiFiConfigLocalAddressType,_G:tunnelWiFiConfigLocalAddress,_H:tunnelWiFiConfigRemoteAddressType,_I:tunnelWiFiConfigRemoteAddress,_J:tunnelWiFiConfigEncapsMethod,_K:tunnelWiFiConfigID,'tunnelWiFiConfigIfIndex':tunnelWiFiConfigIfIndex,'tunnelWiFiConfigStatus':tunnelWiFiConfigStatus,'tunnelWiFiConfigMode':tunnelWiFiConfigMode,'tunnelWiFiConfigDefaultProfile':tunnelWiFiConfigDefaultProfile})