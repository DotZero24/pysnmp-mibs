_J='raisecomRndpInterfaceId'
_I='raisecomRndpDiscoveryDeviceId'
_H='raisecomRndpDiscoveryInterfaceId'
_G='read-write'
_F='EnableVar'
_E='Integer32'
_D='RAISECOM-RNDP-MIB'
_C='mandatory'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomCluster,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomCluster')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_F)
raisecomTopoDiscovery=ModuleIdentity((1,3,6,1,4,1,8886,1,6,2))
class _RaisecomRndpProtocolEnable_Type(EnableVar):defaultValue=2
_RaisecomRndpProtocolEnable_Type.__name__=_F
_RaisecomRndpProtocolEnable_Object=MibScalar
raisecomRndpProtocolEnable=_RaisecomRndpProtocolEnable_Object((1,3,6,1,4,1,8886,1,6,2,1),_RaisecomRndpProtocolEnable_Type())
raisecomRndpProtocolEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomRndpProtocolEnable.setStatus(_C)
_RaisecomRndpDiscoveryTable_Object=MibTable
raisecomRndpDiscoveryTable=_RaisecomRndpDiscoveryTable_Object((1,3,6,1,4,1,8886,1,6,2,2))
if mibBuilder.loadTexts:raisecomRndpDiscoveryTable.setStatus(_A)
_RaisecomRndpDiscoveryEntry_Object=MibTableRow
raisecomRndpDiscoveryEntry=_RaisecomRndpDiscoveryEntry_Object((1,3,6,1,4,1,8886,1,6,2,2,1))
raisecomRndpDiscoveryEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:raisecomRndpDiscoveryEntry.setStatus(_A)
_RaisecomRndpDiscoveryInterfaceId_Type=Integer32
_RaisecomRndpDiscoveryInterfaceId_Object=MibTableColumn
raisecomRndpDiscoveryInterfaceId=_RaisecomRndpDiscoveryInterfaceId_Object((1,3,6,1,4,1,8886,1,6,2,2,1,1),_RaisecomRndpDiscoveryInterfaceId_Type())
raisecomRndpDiscoveryInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryInterfaceId.setStatus(_A)
_RaisecomRndpDiscoveryDeviceId_Type=MacAddress
_RaisecomRndpDiscoveryDeviceId_Object=MibTableColumn
raisecomRndpDiscoveryDeviceId=_RaisecomRndpDiscoveryDeviceId_Object((1,3,6,1,4,1,8886,1,6,2,2,1,2),_RaisecomRndpDiscoveryDeviceId_Type())
raisecomRndpDiscoveryDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryDeviceId.setStatus(_A)
_RaisecomRndpDiscoveryPortId_Type=Integer32
_RaisecomRndpDiscoveryPortId_Object=MibTableColumn
raisecomRndpDiscoveryPortId=_RaisecomRndpDiscoveryPortId_Object((1,3,6,1,4,1,8886,1,6,2,2,1,3),_RaisecomRndpDiscoveryPortId_Type())
raisecomRndpDiscoveryPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryPortId.setStatus(_A)
_RaisecomRndpDiscoveryHostName_Type=OctetString
_RaisecomRndpDiscoveryHostName_Object=MibTableColumn
raisecomRndpDiscoveryHostName=_RaisecomRndpDiscoveryHostName_Object((1,3,6,1,4,1,8886,1,6,2,2,1,4),_RaisecomRndpDiscoveryHostName_Type())
raisecomRndpDiscoveryHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryHostName.setStatus(_A)
_RaisecomRndpDiscoveryPlatformOid_Type=ObjectIdentifier
_RaisecomRndpDiscoveryPlatformOid_Object=MibTableColumn
raisecomRndpDiscoveryPlatformOid=_RaisecomRndpDiscoveryPlatformOid_Object((1,3,6,1,4,1,8886,1,6,2,2,1,5),_RaisecomRndpDiscoveryPlatformOid_Type())
raisecomRndpDiscoveryPlatformOid.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryPlatformOid.setStatus(_A)
_RaisecomRndpDiscoveryVersion_Type=OctetString
_RaisecomRndpDiscoveryVersion_Object=MibTableColumn
raisecomRndpDiscoveryVersion=_RaisecomRndpDiscoveryVersion_Object((1,3,6,1,4,1,8886,1,6,2,2,1,6),_RaisecomRndpDiscoveryVersion_Type())
raisecomRndpDiscoveryVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryVersion.setStatus(_A)
class _RaisecomRndpDiscoveryCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('switch',1),('router',2),('eoa',3),('eos',4),('others',5)))
_RaisecomRndpDiscoveryCapabilities_Type.__name__=_E
_RaisecomRndpDiscoveryCapabilities_Object=MibTableColumn
raisecomRndpDiscoveryCapabilities=_RaisecomRndpDiscoveryCapabilities_Object((1,3,6,1,4,1,8886,1,6,2,2,1,7),_RaisecomRndpDiscoveryCapabilities_Type())
raisecomRndpDiscoveryCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpDiscoveryCapabilities.setStatus(_A)
_RaisecomRndpInterfaceTable_Object=MibTable
raisecomRndpInterfaceTable=_RaisecomRndpInterfaceTable_Object((1,3,6,1,4,1,8886,1,6,2,3))
if mibBuilder.loadTexts:raisecomRndpInterfaceTable.setStatus(_C)
_RaisecomRndpInterfaceEntry_Object=MibTableRow
raisecomRndpInterfaceEntry=_RaisecomRndpInterfaceEntry_Object((1,3,6,1,4,1,8886,1,6,2,3,1))
raisecomRndpInterfaceEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:raisecomRndpInterfaceEntry.setStatus(_C)
_RaisecomRndpInterfaceId_Type=Integer32
_RaisecomRndpInterfaceId_Object=MibTableColumn
raisecomRndpInterfaceId=_RaisecomRndpInterfaceId_Object((1,3,6,1,4,1,8886,1,6,2,3,1,1),_RaisecomRndpInterfaceId_Type())
raisecomRndpInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRndpInterfaceId.setStatus(_C)
_RaisecomRndpInterfaceEnable_Type=EnableVar
_RaisecomRndpInterfaceEnable_Object=MibTableColumn
raisecomRndpInterfaceEnable=_RaisecomRndpInterfaceEnable_Object((1,3,6,1,4,1,8886,1,6,2,3,1,2),_RaisecomRndpInterfaceEnable_Type())
raisecomRndpInterfaceEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomRndpInterfaceEnable.setStatus(_C)
mibBuilder.exportSymbols(_D,**{'raisecomTopoDiscovery':raisecomTopoDiscovery,'raisecomRndpProtocolEnable':raisecomRndpProtocolEnable,'raisecomRndpDiscoveryTable':raisecomRndpDiscoveryTable,'raisecomRndpDiscoveryEntry':raisecomRndpDiscoveryEntry,_H:raisecomRndpDiscoveryInterfaceId,_I:raisecomRndpDiscoveryDeviceId,'raisecomRndpDiscoveryPortId':raisecomRndpDiscoveryPortId,'raisecomRndpDiscoveryHostName':raisecomRndpDiscoveryHostName,'raisecomRndpDiscoveryPlatformOid':raisecomRndpDiscoveryPlatformOid,'raisecomRndpDiscoveryVersion':raisecomRndpDiscoveryVersion,'raisecomRndpDiscoveryCapabilities':raisecomRndpDiscoveryCapabilities,'raisecomRndpInterfaceTable':raisecomRndpInterfaceTable,'raisecomRndpInterfaceEntry':raisecomRndpInterfaceEntry,_J:raisecomRndpInterfaceId,'raisecomRndpInterfaceEnable':raisecomRndpInterfaceEnable})