_O='dsControlPortIndex'
_N='restart'
_M='dsControlSlotIndex'
_L='dsMonitorPortIndex'
_K='dsMonitorSlotIndex'
_J='dsPortIndex'
_I='dsSlotIndex'
_H='on'
_G='DASAN-ACCESS-SLOT-POTS-MIB'
_F='off'
_E='Integer32'
_D='read-only'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dasanMgmt,=mibBuilder.importSymbols('DASAN-SMI','dasanMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_C,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp')
dasanAccessMib=ModuleIdentity((1,3,6,1,4,1,6296,9,100))
if mibBuilder.loadTexts:dasanAccessMib.setRevisions(('2005-02-11 21:00',))
_DasanAccGatewayMIBObjects_ObjectIdentity=ObjectIdentity
dasanAccGatewayMIBObjects=_DasanAccGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2))
_DsAccGwyPots_ObjectIdentity=ObjectIdentity
dsAccGwyPots=_DsAccGwyPots_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1))
_DsAccGwyPotsConfiguration_ObjectIdentity=ObjectIdentity
dsAccGwyPotsConfiguration=_DsAccGwyPotsConfiguration_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,1))
_DsAccGwyConfigPotsSystem_ObjectIdentity=ObjectIdentity
dsAccGwyConfigPotsSystem=_DsAccGwyConfigPotsSystem_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,1,1))
class _DsAccGwyConfigGlobalDigitmap_Type(DisplayString):defaultValue=OctetString('x.T')
_DsAccGwyConfigGlobalDigitmap_Type.__name__=_C
_DsAccGwyConfigGlobalDigitmap_Object=MibScalar
dsAccGwyConfigGlobalDigitmap=_DsAccGwyConfigGlobalDigitmap_Object((1,3,6,1,4,1,6296,9,100,2,1,1,1,1),_DsAccGwyConfigGlobalDigitmap_Type())
dsAccGwyConfigGlobalDigitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAccGwyConfigGlobalDigitmap.setStatus(_A)
class _DsAccGwyConfigGlobalSwitchDhcp_Type(DisplayString):defaultValue=OctetString(_F)
_DsAccGwyConfigGlobalSwitchDhcp_Type.__name__=_C
_DsAccGwyConfigGlobalSwitchDhcp_Object=MibScalar
dsAccGwyConfigGlobalSwitchDhcp=_DsAccGwyConfigGlobalSwitchDhcp_Object((1,3,6,1,4,1,6296,9,100,2,1,1,1,2),_DsAccGwyConfigGlobalSwitchDhcp_Type())
dsAccGwyConfigGlobalSwitchDhcp.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAccGwyConfigGlobalSwitchDhcp.setStatus(_A)
_DsAccGwyConfigPotsSlot_ObjectIdentity=ObjectIdentity
dsAccGwyConfigPotsSlot=_DsAccGwyConfigPotsSlot_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,1,2))
_DsAccGwyConfigSlotTable_Object=MibTable
dsAccGwyConfigSlotTable=_DsAccGwyConfigSlotTable_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1))
if mibBuilder.loadTexts:dsAccGwyConfigSlotTable.setStatus(_A)
_DsAccGwyConfigSlotEntry_Object=MibTableRow
dsAccGwyConfigSlotEntry=_DsAccGwyConfigSlotEntry_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1))
dsAccGwyConfigSlotEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:dsAccGwyConfigSlotEntry.setStatus(_A)
_DsSlotIndex_Type=Integer32
_DsSlotIndex_Object=MibTableColumn
dsSlotIndex=_DsSlotIndex_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,1),_DsSlotIndex_Type())
dsSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSlotIndex.setStatus(_A)
class _DsSlotAddAreaCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_DsSlotAddAreaCode_Type.__name__=_E
_DsSlotAddAreaCode_Object=MibTableColumn
dsSlotAddAreaCode=_DsSlotAddAreaCode_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,2),_DsSlotAddAreaCode_Type())
dsSlotAddAreaCode.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotAddAreaCode.setStatus(_A)
class _DsSlotAreaCode_Type(DisplayString):defaultValue=OctetString('')
_DsSlotAreaCode_Type.__name__=_C
_DsSlotAreaCode_Object=MibTableColumn
dsSlotAreaCode=_DsSlotAreaCode_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,3),_DsSlotAreaCode_Type())
dsSlotAreaCode.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotAreaCode.setStatus(_A)
class _DsSlotAreaCodeAllows_Type(DisplayString):defaultValue=OctetString('')
_DsSlotAreaCodeAllows_Type.__name__=_C
_DsSlotAreaCodeAllows_Object=MibTableColumn
dsSlotAreaCodeAllows=_DsSlotAreaCodeAllows_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,4),_DsSlotAreaCodeAllows_Type())
dsSlotAreaCodeAllows.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotAreaCodeAllows.setStatus(_A)
class _DsSlotAreaCodeExceptions_Type(DisplayString):defaultValue=OctetString('')
_DsSlotAreaCodeExceptions_Type.__name__=_C
_DsSlotAreaCodeExceptions_Object=MibTableColumn
dsSlotAreaCodeExceptions=_DsSlotAreaCodeExceptions_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,5),_DsSlotAreaCodeExceptions_Type())
dsSlotAreaCodeExceptions.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotAreaCodeExceptions.setStatus(_A)
class _DsSlotCodecType_Type(DisplayString):defaultValue=OctetString('')
_DsSlotCodecType_Type.__name__=_C
_DsSlotCodecType_Object=MibTableColumn
dsSlotCodecType=_DsSlotCodecType_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,6),_DsSlotCodecType_Type())
dsSlotCodecType.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotCodecType.setStatus(_A)
_DsSlotCodecPacketizationPeriodG711_Type=Integer32
_DsSlotCodecPacketizationPeriodG711_Object=MibTableColumn
dsSlotCodecPacketizationPeriodG711=_DsSlotCodecPacketizationPeriodG711_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,7),_DsSlotCodecPacketizationPeriodG711_Type())
dsSlotCodecPacketizationPeriodG711.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotCodecPacketizationPeriodG711.setStatus(_A)
_DsSlotCodecPacketizationPeriodG723_Type=Integer32
_DsSlotCodecPacketizationPeriodG723_Object=MibTableColumn
dsSlotCodecPacketizationPeriodG723=_DsSlotCodecPacketizationPeriodG723_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,8),_DsSlotCodecPacketizationPeriodG723_Type())
dsSlotCodecPacketizationPeriodG723.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotCodecPacketizationPeriodG723.setStatus(_A)
_DsSlotCodecPacketizationPeriodG729_Type=Integer32
_DsSlotCodecPacketizationPeriodG729_Object=MibTableColumn
dsSlotCodecPacketizationPeriodG729=_DsSlotCodecPacketizationPeriodG729_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,9),_DsSlotCodecPacketizationPeriodG729_Type())
dsSlotCodecPacketizationPeriodG729.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotCodecPacketizationPeriodG729.setStatus(_A)
class _DsSlotJitterbuffer_Type(DisplayString):defaultValue=OctetString('')
_DsSlotJitterbuffer_Type.__name__=_C
_DsSlotJitterbuffer_Object=MibTableColumn
dsSlotJitterbuffer=_DsSlotJitterbuffer_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,10),_DsSlotJitterbuffer_Type())
dsSlotJitterbuffer.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSlotJitterbuffer.setStatus(_A)
_DsSlotRingonTime_Type=Integer32
_DsSlotRingonTime_Object=MibTableColumn
dsSlotRingonTime=_DsSlotRingonTime_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,11),_DsSlotRingonTime_Type())
dsSlotRingonTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotRingonTime.setStatus(_A)
_DsSlotRingoffTime_Type=Integer32
_DsSlotRingoffTime_Object=MibTableColumn
dsSlotRingoffTime=_DsSlotRingoffTime_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,12),_DsSlotRingoffTime_Type())
dsSlotRingoffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotRingoffTime.setStatus(_A)
_DsSlotHookflashMin_Type=Integer32
_DsSlotHookflashMin_Object=MibTableColumn
dsSlotHookflashMin=_DsSlotHookflashMin_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,13),_DsSlotHookflashMin_Type())
dsSlotHookflashMin.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotHookflashMin.setStatus(_A)
_DsSlotHookflashMax_Type=Integer32
_DsSlotHookflashMax_Object=MibTableColumn
dsSlotHookflashMax=_DsSlotHookflashMax_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,14),_DsSlotHookflashMax_Type())
dsSlotHookflashMax.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotHookflashMax.setStatus(_A)
_DsSlotInterdigitTimeout_Type=Integer32
_DsSlotInterdigitTimeout_Object=MibTableColumn
dsSlotInterdigitTimeout=_DsSlotInterdigitTimeout_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,15),_DsSlotInterdigitTimeout_Type())
dsSlotInterdigitTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotInterdigitTimeout.setStatus(_A)
class _DsSlotEce_Type(DisplayString):defaultValue=OctetString('1')
_DsSlotEce_Type.__name__=_C
_DsSlotEce_Object=MibTableColumn
dsSlotEce=_DsSlotEce_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,16),_DsSlotEce_Type())
dsSlotEce.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSlotEce.setStatus(_A)
class _DsSlotFax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_DsSlotFax_Type.__name__=_E
_DsSlotFax_Object=MibTableColumn
dsSlotFax=_DsSlotFax_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,17),_DsSlotFax_Type())
dsSlotFax.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotFax.setStatus(_A)
class _DsSlotCid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('belcore',1),('ntt',2)))
_DsSlotCid_Type.__name__=_E
_DsSlotCid_Object=MibTableColumn
dsSlotCid=_DsSlotCid_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,18),_DsSlotCid_Type())
dsSlotCid.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotCid.setStatus(_A)
class _DsSlotVad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_DsSlotVad_Type.__name__=_E
_DsSlotVad_Object=MibTableColumn
dsSlotVad=_DsSlotVad_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,19),_DsSlotVad_Type())
dsSlotVad.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotVad.setStatus(_A)
class _DsSlotCng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_DsSlotCng_Type.__name__=_E
_DsSlotCng_Object=MibTableColumn
dsSlotCng=_DsSlotCng_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,20),_DsSlotCng_Type())
dsSlotCng.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotCng.setStatus(_A)
class _DsSlotOobdtmf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_DsSlotOobdtmf_Type.__name__=_E
_DsSlotOobdtmf_Object=MibTableColumn
dsSlotOobdtmf=_DsSlotOobdtmf_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,21),_DsSlotOobdtmf_Type())
dsSlotOobdtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotOobdtmf.setStatus(_A)
class _DsSlotNetworkHostname_Type(DisplayString):defaultValue=OctetString('')
_DsSlotNetworkHostname_Type.__name__=_C
_DsSlotNetworkHostname_Object=MibTableColumn
dsSlotNetworkHostname=_DsSlotNetworkHostname_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,22),_DsSlotNetworkHostname_Type())
dsSlotNetworkHostname.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSlotNetworkHostname.setStatus(_A)
class _DsSlotNetworkDhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),('on-syslog',2)))
_DsSlotNetworkDhcp_Type.__name__=_E
_DsSlotNetworkDhcp_Object=MibTableColumn
dsSlotNetworkDhcp=_DsSlotNetworkDhcp_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,23),_DsSlotNetworkDhcp_Type())
dsSlotNetworkDhcp.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotNetworkDhcp.setStatus(_A)
class _DsSlotNetworkIpaddress_Type(DisplayString):defaultValue=OctetString('192.168.1.2')
_DsSlotNetworkIpaddress_Type.__name__=_C
_DsSlotNetworkIpaddress_Object=MibTableColumn
dsSlotNetworkIpaddress=_DsSlotNetworkIpaddress_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,24),_DsSlotNetworkIpaddress_Type())
dsSlotNetworkIpaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotNetworkIpaddress.setStatus(_A)
class _DsSlotNetworkSubnetmask_Type(DisplayString):defaultValue=OctetString('255.255.255.0')
_DsSlotNetworkSubnetmask_Type.__name__=_C
_DsSlotNetworkSubnetmask_Object=MibTableColumn
dsSlotNetworkSubnetmask=_DsSlotNetworkSubnetmask_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,25),_DsSlotNetworkSubnetmask_Type())
dsSlotNetworkSubnetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotNetworkSubnetmask.setStatus(_A)
class _DsSlotNetworkRouter_Type(DisplayString):defaultValue=OctetString('192.168.1.1')
_DsSlotNetworkRouter_Type.__name__=_C
_DsSlotNetworkRouter_Object=MibTableColumn
dsSlotNetworkRouter=_DsSlotNetworkRouter_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,26),_DsSlotNetworkRouter_Type())
dsSlotNetworkRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotNetworkRouter.setStatus(_A)
class _DsSlotNetworkNameserver_Type(DisplayString):defaultValue=OctetString('168.126.63.1')
_DsSlotNetworkNameserver_Type.__name__=_C
_DsSlotNetworkNameserver_Object=MibTableColumn
dsSlotNetworkNameserver=_DsSlotNetworkNameserver_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,27),_DsSlotNetworkNameserver_Type())
dsSlotNetworkNameserver.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSlotNetworkNameserver.setStatus(_A)
_DsSlotVersion_Type=DisplayString
_DsSlotVersion_Object=MibTableColumn
dsSlotVersion=_DsSlotVersion_Object((1,3,6,1,4,1,6296,9,100,2,1,1,2,1,1,28),_DsSlotVersion_Type())
dsSlotVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dsSlotVersion.setStatus(_A)
_DsAccGwyConfigPotsPort_ObjectIdentity=ObjectIdentity
dsAccGwyConfigPotsPort=_DsAccGwyConfigPotsPort_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,1,3))
_DsAccGwyConfigPortTable_Object=MibTable
dsAccGwyConfigPortTable=_DsAccGwyConfigPortTable_Object((1,3,6,1,4,1,6296,9,100,2,1,1,3,1))
if mibBuilder.loadTexts:dsAccGwyConfigPortTable.setStatus(_A)
_DsAccGwyConfigPortEntry_Object=MibTableRow
dsAccGwyConfigPortEntry=_DsAccGwyConfigPortEntry_Object((1,3,6,1,4,1,6296,9,100,2,1,1,3,1,1))
dsAccGwyConfigPortEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:dsAccGwyConfigPortEntry.setStatus(_A)
_DsPortIndex_Type=Integer32
_DsPortIndex_Object=MibTableColumn
dsPortIndex=_DsPortIndex_Object((1,3,6,1,4,1,6296,9,100,2,1,1,3,1,1,1),_DsPortIndex_Type())
dsPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsPortIndex.setStatus(_A)
_DsPortIvol_Type=Integer32
_DsPortIvol_Object=MibTableColumn
dsPortIvol=_DsPortIvol_Object((1,3,6,1,4,1,6296,9,100,2,1,1,3,1,1,2),_DsPortIvol_Type())
dsPortIvol.setMaxAccess(_B)
if mibBuilder.loadTexts:dsPortIvol.setStatus(_A)
_DsPortOvol_Type=Integer32
_DsPortOvol_Object=MibTableColumn
dsPortOvol=_DsPortOvol_Object((1,3,6,1,4,1,6296,9,100,2,1,1,3,1,1,3),_DsPortOvol_Type())
dsPortOvol.setMaxAccess(_B)
if mibBuilder.loadTexts:dsPortOvol.setStatus(_A)
_DsAccGwyPotsMonitor_ObjectIdentity=ObjectIdentity
dsAccGwyPotsMonitor=_DsAccGwyPotsMonitor_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,2))
_DsAccGwyMonitorPotsSystem_ObjectIdentity=ObjectIdentity
dsAccGwyMonitorPotsSystem=_DsAccGwyMonitorPotsSystem_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,2,1))
_DsMonitorAccGwyUpsStatus_Type=DisplayString
_DsMonitorAccGwyUpsStatus_Object=MibScalar
dsMonitorAccGwyUpsStatus=_DsMonitorAccGwyUpsStatus_Object((1,3,6,1,4,1,6296,9,100,2,1,2,1,1),_DsMonitorAccGwyUpsStatus_Type())
dsMonitorAccGwyUpsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorAccGwyUpsStatus.setStatus(_A)
_DsAccGwyMonitorPotsSlot_ObjectIdentity=ObjectIdentity
dsAccGwyMonitorPotsSlot=_DsAccGwyMonitorPotsSlot_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,2,2))
_DsAccGwyMonitorSlotTable_Object=MibTable
dsAccGwyMonitorSlotTable=_DsAccGwyMonitorSlotTable_Object((1,3,6,1,4,1,6296,9,100,2,1,2,2,1))
if mibBuilder.loadTexts:dsAccGwyMonitorSlotTable.setStatus(_A)
_DsAccGwyMonitorSlotEntry_Object=MibTableRow
dsAccGwyMonitorSlotEntry=_DsAccGwyMonitorSlotEntry_Object((1,3,6,1,4,1,6296,9,100,2,1,2,2,1,1))
dsAccGwyMonitorSlotEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:dsAccGwyMonitorSlotEntry.setStatus(_A)
_DsMonitorSlotIndex_Type=Integer32
_DsMonitorSlotIndex_Object=MibTableColumn
dsMonitorSlotIndex=_DsMonitorSlotIndex_Object((1,3,6,1,4,1,6296,9,100,2,1,2,2,1,1,1),_DsMonitorSlotIndex_Type())
dsMonitorSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorSlotIndex.setStatus(_A)
class _DsMonitorSlotInstallStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('installed',1),('removed',2)))
_DsMonitorSlotInstallStatus_Type.__name__=_E
_DsMonitorSlotInstallStatus_Object=MibTableColumn
dsMonitorSlotInstallStatus=_DsMonitorSlotInstallStatus_Object((1,3,6,1,4,1,6296,9,100,2,1,2,2,1,1,2),_DsMonitorSlotInstallStatus_Type())
dsMonitorSlotInstallStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorSlotInstallStatus.setStatus(_A)
_DsAccGwyMonitorPotsPort_ObjectIdentity=ObjectIdentity
dsAccGwyMonitorPotsPort=_DsAccGwyMonitorPotsPort_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,2,3))
_DsAccGwyMonitorPortTable_Object=MibTable
dsAccGwyMonitorPortTable=_DsAccGwyMonitorPortTable_Object((1,3,6,1,4,1,6296,9,100,2,1,2,3,1))
if mibBuilder.loadTexts:dsAccGwyMonitorPortTable.setStatus(_A)
_DsAccGwyMonitorPortEntry_Object=MibTableRow
dsAccGwyMonitorPortEntry=_DsAccGwyMonitorPortEntry_Object((1,3,6,1,4,1,6296,9,100,2,1,2,3,1,1))
dsAccGwyMonitorPortEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:dsAccGwyMonitorPortEntry.setStatus(_A)
_DsMonitorPortIndex_Type=Integer32
_DsMonitorPortIndex_Object=MibTableColumn
dsMonitorPortIndex=_DsMonitorPortIndex_Object((1,3,6,1,4,1,6296,9,100,2,1,2,3,1,1,1),_DsMonitorPortIndex_Type())
dsMonitorPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorPortIndex.setStatus(_A)
_DsMonitorPortStatus_Type=DisplayString
_DsMonitorPortStatus_Object=MibTableColumn
dsMonitorPortStatus=_DsMonitorPortStatus_Object((1,3,6,1,4,1,6296,9,100,2,1,2,3,1,1,2),_DsMonitorPortStatus_Type())
dsMonitorPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorPortStatus.setStatus(_A)
_DsMonitorPortStatistics_Type=DisplayString
_DsMonitorPortStatistics_Object=MibTableColumn
dsMonitorPortStatistics=_DsMonitorPortStatistics_Object((1,3,6,1,4,1,6296,9,100,2,1,2,3,1,1,3),_DsMonitorPortStatistics_Type())
dsMonitorPortStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:dsMonitorPortStatistics.setStatus(_A)
_DsAccGwyPotsControl_ObjectIdentity=ObjectIdentity
dsAccGwyPotsControl=_DsAccGwyPotsControl_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,3))
_DsAccGwyControlPotsSlot_ObjectIdentity=ObjectIdentity
dsAccGwyControlPotsSlot=_DsAccGwyControlPotsSlot_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,3,1))
_DsAccGwyControlSlotTable_Object=MibTable
dsAccGwyControlSlotTable=_DsAccGwyControlSlotTable_Object((1,3,6,1,4,1,6296,9,100,2,1,3,1,1))
if mibBuilder.loadTexts:dsAccGwyControlSlotTable.setStatus(_A)
_DsAccGwyControlSlotEntry_Object=MibTableRow
dsAccGwyControlSlotEntry=_DsAccGwyControlSlotEntry_Object((1,3,6,1,4,1,6296,9,100,2,1,3,1,1,1))
dsAccGwyControlSlotEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:dsAccGwyControlSlotEntry.setStatus(_A)
_DsControlSlotIndex_Type=Integer32
_DsControlSlotIndex_Object=MibTableColumn
dsControlSlotIndex=_DsControlSlotIndex_Object((1,3,6,1,4,1,6296,9,100,2,1,3,1,1,1,1),_DsControlSlotIndex_Type())
dsControlSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsControlSlotIndex.setStatus(_A)
class _DsControlSlotPotsRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_N,1))
_DsControlSlotPotsRestart_Type.__name__=_E
_DsControlSlotPotsRestart_Object=MibTableColumn
dsControlSlotPotsRestart=_DsControlSlotPotsRestart_Object((1,3,6,1,4,1,6296,9,100,2,1,3,1,1,1,2),_DsControlSlotPotsRestart_Type())
dsControlSlotPotsRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:dsControlSlotPotsRestart.setStatus(_A)
class _DsControlSlotRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_N,1))
_DsControlSlotRestart_Type.__name__=_E
_DsControlSlotRestart_Object=MibTableColumn
dsControlSlotRestart=_DsControlSlotRestart_Object((1,3,6,1,4,1,6296,9,100,2,1,3,1,1,1,3),_DsControlSlotRestart_Type())
dsControlSlotRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:dsControlSlotRestart.setStatus(_A)
_DsAccGwyControlPotsPort_ObjectIdentity=ObjectIdentity
dsAccGwyControlPotsPort=_DsAccGwyControlPotsPort_ObjectIdentity((1,3,6,1,4,1,6296,9,100,2,1,3,2))
_DsAccGwyControlPortTable_Object=MibTable
dsAccGwyControlPortTable=_DsAccGwyControlPortTable_Object((1,3,6,1,4,1,6296,9,100,2,1,3,2,1))
if mibBuilder.loadTexts:dsAccGwyControlPortTable.setStatus(_A)
_DsAccGwyControlPortEntry_Object=MibTableRow
dsAccGwyControlPortEntry=_DsAccGwyControlPortEntry_Object((1,3,6,1,4,1,6296,9,100,2,1,3,2,1,1))
dsAccGwyControlPortEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:dsAccGwyControlPortEntry.setStatus(_A)
_DsControlPortIndex_Type=Integer32
_DsControlPortIndex_Object=MibTableColumn
dsControlPortIndex=_DsControlPortIndex_Object((1,3,6,1,4,1,6296,9,100,2,1,3,2,1,1,1),_DsControlPortIndex_Type())
dsControlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsControlPortIndex.setStatus(_A)
class _DsControlPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_DsControlPortReset_Type.__name__=_E
_DsControlPortReset_Object=MibTableColumn
dsControlPortReset=_DsControlPortReset_Object((1,3,6,1,4,1,6296,9,100,2,1,3,2,1,1,2),_DsControlPortReset_Type())
dsControlPortReset.setMaxAccess(_B)
if mibBuilder.loadTexts:dsControlPortReset.setStatus(_A)
class _DsControlPortPortBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unblock',0),('block',1)))
_DsControlPortPortBlock_Type.__name__=_E
_DsControlPortPortBlock_Object=MibTableColumn
dsControlPortPortBlock=_DsControlPortPortBlock_Object((1,3,6,1,4,1,6296,9,100,2,1,3,2,1,1,3),_DsControlPortPortBlock_Type())
dsControlPortPortBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:dsControlPortPortBlock.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'dasanAccessMib':dasanAccessMib,'dasanAccGatewayMIBObjects':dasanAccGatewayMIBObjects,'dsAccGwyPots':dsAccGwyPots,'dsAccGwyPotsConfiguration':dsAccGwyPotsConfiguration,'dsAccGwyConfigPotsSystem':dsAccGwyConfigPotsSystem,'dsAccGwyConfigGlobalDigitmap':dsAccGwyConfigGlobalDigitmap,'dsAccGwyConfigGlobalSwitchDhcp':dsAccGwyConfigGlobalSwitchDhcp,'dsAccGwyConfigPotsSlot':dsAccGwyConfigPotsSlot,'dsAccGwyConfigSlotTable':dsAccGwyConfigSlotTable,'dsAccGwyConfigSlotEntry':dsAccGwyConfigSlotEntry,_I:dsSlotIndex,'dsSlotAddAreaCode':dsSlotAddAreaCode,'dsSlotAreaCode':dsSlotAreaCode,'dsSlotAreaCodeAllows':dsSlotAreaCodeAllows,'dsSlotAreaCodeExceptions':dsSlotAreaCodeExceptions,'dsSlotCodecType':dsSlotCodecType,'dsSlotCodecPacketizationPeriodG711':dsSlotCodecPacketizationPeriodG711,'dsSlotCodecPacketizationPeriodG723':dsSlotCodecPacketizationPeriodG723,'dsSlotCodecPacketizationPeriodG729':dsSlotCodecPacketizationPeriodG729,'dsSlotJitterbuffer':dsSlotJitterbuffer,'dsSlotRingonTime':dsSlotRingonTime,'dsSlotRingoffTime':dsSlotRingoffTime,'dsSlotHookflashMin':dsSlotHookflashMin,'dsSlotHookflashMax':dsSlotHookflashMax,'dsSlotInterdigitTimeout':dsSlotInterdigitTimeout,'dsSlotEce':dsSlotEce,'dsSlotFax':dsSlotFax,'dsSlotCid':dsSlotCid,'dsSlotVad':dsSlotVad,'dsSlotCng':dsSlotCng,'dsSlotOobdtmf':dsSlotOobdtmf,'dsSlotNetworkHostname':dsSlotNetworkHostname,'dsSlotNetworkDhcp':dsSlotNetworkDhcp,'dsSlotNetworkIpaddress':dsSlotNetworkIpaddress,'dsSlotNetworkSubnetmask':dsSlotNetworkSubnetmask,'dsSlotNetworkRouter':dsSlotNetworkRouter,'dsSlotNetworkNameserver':dsSlotNetworkNameserver,'dsSlotVersion':dsSlotVersion,'dsAccGwyConfigPotsPort':dsAccGwyConfigPotsPort,'dsAccGwyConfigPortTable':dsAccGwyConfigPortTable,'dsAccGwyConfigPortEntry':dsAccGwyConfigPortEntry,_J:dsPortIndex,'dsPortIvol':dsPortIvol,'dsPortOvol':dsPortOvol,'dsAccGwyPotsMonitor':dsAccGwyPotsMonitor,'dsAccGwyMonitorPotsSystem':dsAccGwyMonitorPotsSystem,'dsMonitorAccGwyUpsStatus':dsMonitorAccGwyUpsStatus,'dsAccGwyMonitorPotsSlot':dsAccGwyMonitorPotsSlot,'dsAccGwyMonitorSlotTable':dsAccGwyMonitorSlotTable,'dsAccGwyMonitorSlotEntry':dsAccGwyMonitorSlotEntry,_K:dsMonitorSlotIndex,'dsMonitorSlotInstallStatus':dsMonitorSlotInstallStatus,'dsAccGwyMonitorPotsPort':dsAccGwyMonitorPotsPort,'dsAccGwyMonitorPortTable':dsAccGwyMonitorPortTable,'dsAccGwyMonitorPortEntry':dsAccGwyMonitorPortEntry,_L:dsMonitorPortIndex,'dsMonitorPortStatus':dsMonitorPortStatus,'dsMonitorPortStatistics':dsMonitorPortStatistics,'dsAccGwyPotsControl':dsAccGwyPotsControl,'dsAccGwyControlPotsSlot':dsAccGwyControlPotsSlot,'dsAccGwyControlSlotTable':dsAccGwyControlSlotTable,'dsAccGwyControlSlotEntry':dsAccGwyControlSlotEntry,_M:dsControlSlotIndex,'dsControlSlotPotsRestart':dsControlSlotPotsRestart,'dsControlSlotRestart':dsControlSlotRestart,'dsAccGwyControlPotsPort':dsAccGwyControlPotsPort,'dsAccGwyControlPortTable':dsAccGwyControlPortTable,'dsAccGwyControlPortEntry':dsAccGwyControlPortEntry,_O:dsControlPortIndex,'dsControlPortReset':dsControlPortReset,'dsControlPortPortBlock':dsControlPortPortBlock})