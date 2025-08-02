_E='LEFTHAND-NETWORKS-NUS-COMMON-NETWORK-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonNetwork,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonNetwork')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonNetworkModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,5))
_NetworkDeviceCount_Type=Integer32
_NetworkDeviceCount_Object=MibScalar
networkDeviceCount=_NetworkDeviceCount_Object((1,3,6,1,4,1,9804,3,1,1,2,2,1),_NetworkDeviceCount_Type())
networkDeviceCount.setMaxAccess(_B)
if mibBuilder.loadTexts:networkDeviceCount.setStatus(_A)
_NetworkDeviceTable_Object=MibTable
networkDeviceTable=_NetworkDeviceTable_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2))
if mibBuilder.loadTexts:networkDeviceTable.setStatus(_A)
_NetworkDeviceEntry_Object=MibTableRow
networkDeviceEntry=_NetworkDeviceEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1))
networkDeviceEntry.setIndexNames((0,_E,'networkIndex'))
if mibBuilder.loadTexts:networkDeviceEntry.setStatus(_A)
_NetworkDeviceIndex_Type=Integer32
_NetworkDeviceIndex_Object=MibTableColumn
networkDeviceIndex=_NetworkDeviceIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,1),_NetworkDeviceIndex_Type())
networkDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:networkDeviceIndex.setStatus(_A)
_NetworkDeviceName_Type=OctetString
_NetworkDeviceName_Object=MibTableColumn
networkDeviceName=_NetworkDeviceName_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,6),_NetworkDeviceName_Type())
networkDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:networkDeviceName.setStatus(_A)
_NetworkDeviceIpAddress_Type=IpAddress
_NetworkDeviceIpAddress_Object=MibTableColumn
networkDeviceIpAddress=_NetworkDeviceIpAddress_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,7),_NetworkDeviceIpAddress_Type())
networkDeviceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:networkDeviceIpAddress.setStatus(_A)
_NetworkDeviceMask_Type=IpAddress
_NetworkDeviceMask_Object=MibTableColumn
networkDeviceMask=_NetworkDeviceMask_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,8),_NetworkDeviceMask_Type())
networkDeviceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:networkDeviceMask.setStatus(_A)
_NetworkDeviceDefaultGateway_Type=IpAddress
_NetworkDeviceDefaultGateway_Object=MibTableColumn
networkDeviceDefaultGateway=_NetworkDeviceDefaultGateway_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,9),_NetworkDeviceDefaultGateway_Type())
networkDeviceDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:networkDeviceDefaultGateway.setStatus(_A)
class _NetworkDeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('auto',2),('static',3),('slave',4)))
_NetworkDeviceMode_Type.__name__=_D
_NetworkDeviceMode_Object=MibTableColumn
networkDeviceMode=_NetworkDeviceMode_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,10),_NetworkDeviceMode_Type())
networkDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:networkDeviceMode.setStatus(_A)
_NetworkDeviceStatus_Type=OctetString
_NetworkDeviceStatus_Object=MibTableColumn
networkDeviceStatus=_NetworkDeviceStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,2,2,1,11),_NetworkDeviceStatus_Type())
networkDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:networkDeviceStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'lhnNusCommonNetworkModule':lhnNusCommonNetworkModule,'networkDeviceCount':networkDeviceCount,'networkDeviceTable':networkDeviceTable,'networkDeviceEntry':networkDeviceEntry,'networkDeviceIndex':networkDeviceIndex,'networkDeviceName':networkDeviceName,'networkDeviceIpAddress':networkDeviceIpAddress,'networkDeviceMask':networkDeviceMask,'networkDeviceDefaultGateway':networkDeviceDefaultGateway,'networkDeviceMode':networkDeviceMode,'networkDeviceStatus':networkDeviceStatus})