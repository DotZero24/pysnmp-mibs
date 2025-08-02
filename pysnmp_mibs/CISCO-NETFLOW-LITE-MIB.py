_A4='cnlIfMonitorInfoGroup'
_A3='cnlSamplerInfoGroup'
_A2='cnlExporterInfoGroup'
_A1='cnlIfMonitorRowStatus'
_A0='cnlIfMonitorStorageType'
_z='cnlIfMonitorPktsDropped'
_y='cnlIfMonitorPktsExported'
_x='cnlIfMonitorPktsObserved'
_w='cnlIfAveragePacketSizeUsed'
_v='cnlIfAveragePacketSizeObserved'
_u='cnlIfAveragePacketSize'
_t='cnlIfExporterName'
_s='cnlIfSamplerName'
_r='cnlIfMonitorActiveStatus'
_q='cnlSamplerRowStatus'
_p='cnlSamplerStorageType'
_o='cnlSamplerPacketOffset'
_n='cnlSamplerPacketSectionSize'
_m='cnlSamplerPacketRate'
_l='cnlMaxSamplerAllowed'
_k='cnlExporterRowStatus'
_j='cnlExporterStorageType'
_i='cnlPacketExported'
_h='cnlExportProtocol'
_g='cnlExportInterfaceTableTimeout'
_f='cnlExportSamplerTableTimeout'
_e='cnlExportTemplateTimeout'
_d='cnlExportDscp'
_c='cnlExportCos'
_b='cnlExportTtl'
_a='cnlExportVrf'
_Z='cnlExportSourceUdpPort'
_Y='cnlExportSourceAddr'
_X='cnlExportDestinationUdpLoadShare'
_W='cnlExportDestinationUdpPort'
_V='cnlExportDestinationAddr'
_U='cnlExportAddrType'
_T='cnlMaxExporterAllowed'
_S='cnlIfMonitorSessionName'
_R='cnlSamplerName'
_Q='cnlExporterName'
_P='InetPortNumber'
_O='InetAddressType'
_N='ifIndex'
_M='IF-MIB'
_L='Layer2Cos'
_K='CiscoVrfName'
_J='seconds'
_I='not-accessible'
_H='Integer32'
_G='StorageType'
_F='SnmpAdminString'
_E='read-only'
_D='Unsigned32'
_C='read-create'
_B='CISCO-NETFLOW-LITE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoVrfName,Layer2Cos=mibBuilder.importSymbols('CISCO-TC',_K,_L)
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
ifIndex,=mibBuilder.importSymbols(_M,_N)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_O,_P)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_G,'TextualConvention')
ciscoNetflowLiteMIB=ModuleIdentity((1,3,6,1,4,1,9,9,776))
if mibBuilder.loadTexts:ciscoNetflowLiteMIB.setRevisions(('2011-09-14 00:00',))
_CiscoNetflowLiteMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNetflowLiteMIBNotifs=_CiscoNetflowLiteMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,776,0))
_CiscoNetflowLiteMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNetflowLiteMIBObjects=_CiscoNetflowLiteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,776,1))
_CnlExporter_ObjectIdentity=ObjectIdentity
cnlExporter=_CnlExporter_ObjectIdentity((1,3,6,1,4,1,9,9,776,1,1))
_CnlMaxExporterAllowed_Type=Unsigned32
_CnlMaxExporterAllowed_Object=MibScalar
cnlMaxExporterAllowed=_CnlMaxExporterAllowed_Object((1,3,6,1,4,1,9,9,776,1,1,1),_CnlMaxExporterAllowed_Type())
cnlMaxExporterAllowed.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlMaxExporterAllowed.setStatus(_A)
_CnlExporterTable_Object=MibTable
cnlExporterTable=_CnlExporterTable_Object((1,3,6,1,4,1,9,9,776,1,1,2))
if mibBuilder.loadTexts:cnlExporterTable.setStatus(_A)
_CnlExporterEntry_Object=MibTableRow
cnlExporterEntry=_CnlExporterEntry_Object((1,3,6,1,4,1,9,9,776,1,1,2,1))
cnlExporterEntry.setIndexNames((1,_B,_Q))
if mibBuilder.loadTexts:cnlExporterEntry.setStatus(_A)
class _CnlExporterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnlExporterName_Type.__name__=_F
_CnlExporterName_Object=MibTableColumn
cnlExporterName=_CnlExporterName_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,1),_CnlExporterName_Type())
cnlExporterName.setMaxAccess(_I)
if mibBuilder.loadTexts:cnlExporterName.setStatus(_A)
class _CnlExportAddrType_Type(InetAddressType):defaultValue=1
_CnlExportAddrType_Type.__name__=_O
_CnlExportAddrType_Object=MibTableColumn
cnlExportAddrType=_CnlExportAddrType_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,2),_CnlExportAddrType_Type())
cnlExportAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportAddrType.setStatus(_A)
_CnlExportDestinationAddr_Type=InetAddress
_CnlExportDestinationAddr_Object=MibTableColumn
cnlExportDestinationAddr=_CnlExportDestinationAddr_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,3),_CnlExportDestinationAddr_Type())
cnlExportDestinationAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportDestinationAddr.setStatus(_A)
class _CnlExportDestinationUdpPort_Type(InetPortNumber):defaultValue=0
_CnlExportDestinationUdpPort_Type.__name__=_P
_CnlExportDestinationUdpPort_Object=MibTableColumn
cnlExportDestinationUdpPort=_CnlExportDestinationUdpPort_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,4),_CnlExportDestinationUdpPort_Type())
cnlExportDestinationUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportDestinationUdpPort.setStatus(_A)
class _CnlExportDestinationUdpLoadShare_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CnlExportDestinationUdpLoadShare_Type.__name__=_D
_CnlExportDestinationUdpLoadShare_Object=MibTableColumn
cnlExportDestinationUdpLoadShare=_CnlExportDestinationUdpLoadShare_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,5),_CnlExportDestinationUdpLoadShare_Type())
cnlExportDestinationUdpLoadShare.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportDestinationUdpLoadShare.setStatus(_A)
_CnlExportSourceAddr_Type=InetAddress
_CnlExportSourceAddr_Object=MibTableColumn
cnlExportSourceAddr=_CnlExportSourceAddr_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,6),_CnlExportSourceAddr_Type())
cnlExportSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportSourceAddr.setStatus(_A)
_CnlExportSourceUdpPort_Type=InetPortNumber
_CnlExportSourceUdpPort_Object=MibTableColumn
cnlExportSourceUdpPort=_CnlExportSourceUdpPort_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,7),_CnlExportSourceUdpPort_Type())
cnlExportSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportSourceUdpPort.setStatus(_A)
class _CnlExportVrf_Type(CiscoVrfName):defaultValue=OctetString('')
_CnlExportVrf_Type.__name__=_K
_CnlExportVrf_Object=MibTableColumn
cnlExportVrf=_CnlExportVrf_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,8),_CnlExportVrf_Type())
cnlExportVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportVrf.setStatus(_A)
class _CnlExportTtl_Type(Unsigned32):defaultValue=254;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_CnlExportTtl_Type.__name__=_D
_CnlExportTtl_Object=MibTableColumn
cnlExportTtl=_CnlExportTtl_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,9),_CnlExportTtl_Type())
cnlExportTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportTtl.setStatus(_A)
class _CnlExportCos_Type(Layer2Cos):defaultValue=0
_CnlExportCos_Type.__name__=_L
_CnlExportCos_Object=MibTableColumn
cnlExportCos=_CnlExportCos_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,10),_CnlExportCos_Type())
cnlExportCos.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportCos.setStatus(_A)
class _CnlExportDscp_Type(Dscp):defaultValue=0
_CnlExportDscp_Type.__name__='Dscp'
_CnlExportDscp_Object=MibTableColumn
cnlExportDscp=_CnlExportDscp_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,11),_CnlExportDscp_Type())
cnlExportDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportDscp.setStatus(_A)
class _CnlExportTemplateTimeout_Type(Unsigned32):defaultValue=1800
_CnlExportTemplateTimeout_Type.__name__=_D
_CnlExportTemplateTimeout_Object=MibTableColumn
cnlExportTemplateTimeout=_CnlExportTemplateTimeout_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,12),_CnlExportTemplateTimeout_Type())
cnlExportTemplateTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportTemplateTimeout.setStatus(_A)
if mibBuilder.loadTexts:cnlExportTemplateTimeout.setUnits(_J)
class _CnlExportSamplerTableTimeout_Type(Unsigned32):defaultValue=1800
_CnlExportSamplerTableTimeout_Type.__name__=_D
_CnlExportSamplerTableTimeout_Object=MibTableColumn
cnlExportSamplerTableTimeout=_CnlExportSamplerTableTimeout_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,13),_CnlExportSamplerTableTimeout_Type())
cnlExportSamplerTableTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportSamplerTableTimeout.setStatus(_A)
if mibBuilder.loadTexts:cnlExportSamplerTableTimeout.setUnits(_J)
class _CnlExportInterfaceTableTimeout_Type(Unsigned32):defaultValue=1800
_CnlExportInterfaceTableTimeout_Type.__name__=_D
_CnlExportInterfaceTableTimeout_Object=MibTableColumn
cnlExportInterfaceTableTimeout=_CnlExportInterfaceTableTimeout_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,14),_CnlExportInterfaceTableTimeout_Type())
cnlExportInterfaceTableTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportInterfaceTableTimeout.setStatus(_A)
if mibBuilder.loadTexts:cnlExportInterfaceTableTimeout.setUnits(_J)
class _CnlExportProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipFix',1),('netflowV9',2)))
_CnlExportProtocol_Type.__name__=_H
_CnlExportProtocol_Object=MibTableColumn
cnlExportProtocol=_CnlExportProtocol_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,15),_CnlExportProtocol_Type())
cnlExportProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExportProtocol.setStatus(_A)
_CnlPacketExported_Type=Counter64
_CnlPacketExported_Object=MibTableColumn
cnlPacketExported=_CnlPacketExported_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,16),_CnlPacketExported_Type())
cnlPacketExported.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlPacketExported.setStatus(_A)
class _CnlExporterStorageType_Type(StorageType):defaultValue=2
_CnlExporterStorageType_Type.__name__=_G
_CnlExporterStorageType_Object=MibTableColumn
cnlExporterStorageType=_CnlExporterStorageType_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,17),_CnlExporterStorageType_Type())
cnlExporterStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExporterStorageType.setStatus(_A)
_CnlExporterRowStatus_Type=RowStatus
_CnlExporterRowStatus_Object=MibTableColumn
cnlExporterRowStatus=_CnlExporterRowStatus_Object((1,3,6,1,4,1,9,9,776,1,1,2,1,18),_CnlExporterRowStatus_Type())
cnlExporterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlExporterRowStatus.setStatus(_A)
_CnlSampler_ObjectIdentity=ObjectIdentity
cnlSampler=_CnlSampler_ObjectIdentity((1,3,6,1,4,1,9,9,776,1,2))
_CnlMaxSamplerAllowed_Type=Unsigned32
_CnlMaxSamplerAllowed_Object=MibScalar
cnlMaxSamplerAllowed=_CnlMaxSamplerAllowed_Object((1,3,6,1,4,1,9,9,776,1,2,1),_CnlMaxSamplerAllowed_Type())
cnlMaxSamplerAllowed.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlMaxSamplerAllowed.setStatus(_A)
_CnlSamplerTable_Object=MibTable
cnlSamplerTable=_CnlSamplerTable_Object((1,3,6,1,4,1,9,9,776,1,2,2))
if mibBuilder.loadTexts:cnlSamplerTable.setStatus(_A)
_CnlSamplerEntry_Object=MibTableRow
cnlSamplerEntry=_CnlSamplerEntry_Object((1,3,6,1,4,1,9,9,776,1,2,2,1))
cnlSamplerEntry.setIndexNames((1,_B,_R))
if mibBuilder.loadTexts:cnlSamplerEntry.setStatus(_A)
class _CnlSamplerName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnlSamplerName_Type.__name__=_F
_CnlSamplerName_Object=MibTableColumn
cnlSamplerName=_CnlSamplerName_Object((1,3,6,1,4,1,9,9,776,1,2,2,1,1),_CnlSamplerName_Type())
cnlSamplerName.setMaxAccess(_I)
if mibBuilder.loadTexts:cnlSamplerName.setStatus(_A)
class _CnlSamplerPacketRate_Type(Unsigned32):defaultValue=1
_CnlSamplerPacketRate_Type.__name__=_D
_CnlSamplerPacketRate_Object=MibTableColumn
cnlSamplerPacketRate=_CnlSamplerPacketRate_Object((1,3,6,1,4,1,9,9,776,1,2,2,1,2),_CnlSamplerPacketRate_Type())
cnlSamplerPacketRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlSamplerPacketRate.setStatus(_A)
class _CnlSamplerPacketSectionSize_Type(Unsigned32):defaultValue=64
_CnlSamplerPacketSectionSize_Type.__name__=_D
_CnlSamplerPacketSectionSize_Object=MibTableColumn
cnlSamplerPacketSectionSize=_CnlSamplerPacketSectionSize_Object((1,3,6,1,4,1,9,9,776,1,2,2,1,3),_CnlSamplerPacketSectionSize_Type())
cnlSamplerPacketSectionSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlSamplerPacketSectionSize.setStatus(_A)
if mibBuilder.loadTexts:cnlSamplerPacketSectionSize.setUnits('bytes')
class _CnlSamplerPacketOffset_Type(Unsigned32):defaultValue=0
_CnlSamplerPacketOffset_Type.__name__=_D
_CnlSamplerPacketOffset_Object=MibTableColumn
cnlSamplerPacketOffset=_CnlSamplerPacketOffset_Object((1,3,6,1,4,1,9,9,776,1,2,2,1,4),_CnlSamplerPacketOffset_Type())
cnlSamplerPacketOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlSamplerPacketOffset.setStatus(_A)
class _CnlSamplerStorageType_Type(StorageType):defaultValue=2
_CnlSamplerStorageType_Type.__name__=_G
_CnlSamplerStorageType_Object=MibTableColumn
cnlSamplerStorageType=_CnlSamplerStorageType_Object((1,3,6,1,4,1,9,9,776,1,2,2,1,5),_CnlSamplerStorageType_Type())
cnlSamplerStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlSamplerStorageType.setStatus(_A)
_CnlSamplerRowStatus_Type=RowStatus
_CnlSamplerRowStatus_Object=MibTableColumn
cnlSamplerRowStatus=_CnlSamplerRowStatus_Object((1,3,6,1,4,1,9,9,776,1,2,2,1,6),_CnlSamplerRowStatus_Type())
cnlSamplerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlSamplerRowStatus.setStatus(_A)
_CnlMonitor_ObjectIdentity=ObjectIdentity
cnlMonitor=_CnlMonitor_ObjectIdentity((1,3,6,1,4,1,9,9,776,1,3))
_CnlIfMonitorTable_Object=MibTable
cnlIfMonitorTable=_CnlIfMonitorTable_Object((1,3,6,1,4,1,9,9,776,1,3,1))
if mibBuilder.loadTexts:cnlIfMonitorTable.setStatus(_A)
_CnlIfMonitorEntry_Object=MibTableRow
cnlIfMonitorEntry=_CnlIfMonitorEntry_Object((1,3,6,1,4,1,9,9,776,1,3,1,1))
cnlIfMonitorEntry.setIndexNames((0,_M,_N),(1,_B,_S))
if mibBuilder.loadTexts:cnlIfMonitorEntry.setStatus(_A)
class _CnlIfMonitorSessionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnlIfMonitorSessionName_Type.__name__=_F
_CnlIfMonitorSessionName_Object=MibTableColumn
cnlIfMonitorSessionName=_CnlIfMonitorSessionName_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,1),_CnlIfMonitorSessionName_Type())
cnlIfMonitorSessionName.setMaxAccess(_I)
if mibBuilder.loadTexts:cnlIfMonitorSessionName.setStatus(_A)
class _CnlIfMonitorActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_CnlIfMonitorActiveStatus_Type.__name__=_H
_CnlIfMonitorActiveStatus_Object=MibTableColumn
cnlIfMonitorActiveStatus=_CnlIfMonitorActiveStatus_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,2),_CnlIfMonitorActiveStatus_Type())
cnlIfMonitorActiveStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlIfMonitorActiveStatus.setStatus(_A)
_CnlIfSamplerName_Type=SnmpAdminString
_CnlIfSamplerName_Object=MibTableColumn
cnlIfSamplerName=_CnlIfSamplerName_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,3),_CnlIfSamplerName_Type())
cnlIfSamplerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlIfSamplerName.setStatus(_A)
_CnlIfExporterName_Type=SnmpAdminString
_CnlIfExporterName_Object=MibTableColumn
cnlIfExporterName=_CnlIfExporterName_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,4),_CnlIfExporterName_Type())
cnlIfExporterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlIfExporterName.setStatus(_A)
class _CnlIfAveragePacketSize_Type(Unsigned32):defaultValue=0
_CnlIfAveragePacketSize_Type.__name__=_D
_CnlIfAveragePacketSize_Object=MibTableColumn
cnlIfAveragePacketSize=_CnlIfAveragePacketSize_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,5),_CnlIfAveragePacketSize_Type())
cnlIfAveragePacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlIfAveragePacketSize.setStatus(_A)
_CnlIfAveragePacketSizeObserved_Type=Unsigned32
_CnlIfAveragePacketSizeObserved_Object=MibTableColumn
cnlIfAveragePacketSizeObserved=_CnlIfAveragePacketSizeObserved_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,6),_CnlIfAveragePacketSizeObserved_Type())
cnlIfAveragePacketSizeObserved.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlIfAveragePacketSizeObserved.setStatus(_A)
_CnlIfAveragePacketSizeUsed_Type=Unsigned32
_CnlIfAveragePacketSizeUsed_Object=MibTableColumn
cnlIfAveragePacketSizeUsed=_CnlIfAveragePacketSizeUsed_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,7),_CnlIfAveragePacketSizeUsed_Type())
cnlIfAveragePacketSizeUsed.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlIfAveragePacketSizeUsed.setStatus(_A)
_CnlIfMonitorPktsObserved_Type=Counter64
_CnlIfMonitorPktsObserved_Object=MibTableColumn
cnlIfMonitorPktsObserved=_CnlIfMonitorPktsObserved_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,8),_CnlIfMonitorPktsObserved_Type())
cnlIfMonitorPktsObserved.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlIfMonitorPktsObserved.setStatus(_A)
_CnlIfMonitorPktsExported_Type=Counter64
_CnlIfMonitorPktsExported_Object=MibTableColumn
cnlIfMonitorPktsExported=_CnlIfMonitorPktsExported_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,9),_CnlIfMonitorPktsExported_Type())
cnlIfMonitorPktsExported.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlIfMonitorPktsExported.setStatus(_A)
_CnlIfMonitorPktsDropped_Type=Counter64
_CnlIfMonitorPktsDropped_Object=MibTableColumn
cnlIfMonitorPktsDropped=_CnlIfMonitorPktsDropped_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,10),_CnlIfMonitorPktsDropped_Type())
cnlIfMonitorPktsDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:cnlIfMonitorPktsDropped.setStatus(_A)
class _CnlIfMonitorStorageType_Type(StorageType):defaultValue=2
_CnlIfMonitorStorageType_Type.__name__=_G
_CnlIfMonitorStorageType_Object=MibTableColumn
cnlIfMonitorStorageType=_CnlIfMonitorStorageType_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,11),_CnlIfMonitorStorageType_Type())
cnlIfMonitorStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlIfMonitorStorageType.setStatus(_A)
_CnlIfMonitorRowStatus_Type=RowStatus
_CnlIfMonitorRowStatus_Object=MibTableColumn
cnlIfMonitorRowStatus=_CnlIfMonitorRowStatus_Object((1,3,6,1,4,1,9,9,776,1,3,1,1,12),_CnlIfMonitorRowStatus_Type())
cnlIfMonitorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnlIfMonitorRowStatus.setStatus(_A)
_CiscoNetflowLiteMIBConform_ObjectIdentity=ObjectIdentity
ciscoNetflowLiteMIBConform=_CiscoNetflowLiteMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,776,2))
_CiscoNetflowLiteMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNetflowLiteMIBCompliances=_CiscoNetflowLiteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,776,2,1))
_CiscoNetflowLiteMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNetflowLiteMIBGroups=_CiscoNetflowLiteMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,776,2,2))
cnlExporterInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,776,2,2,1))
cnlExporterInfoGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cnlExporterInfoGroup.setStatus(_A)
cnlSamplerInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,776,2,2,2))
cnlSamplerInfoGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cnlSamplerInfoGroup.setStatus(_A)
cnlIfMonitorInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,776,2,2,3))
cnlIfMonitorInfoGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:cnlIfMonitorInfoGroup.setStatus(_A)
ciscoNetflowLiteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,776,2,1,1))
ciscoNetflowLiteMIBCompliance.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoNetflowLiteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNetflowLiteMIB':ciscoNetflowLiteMIB,'ciscoNetflowLiteMIBNotifs':ciscoNetflowLiteMIBNotifs,'ciscoNetflowLiteMIBObjects':ciscoNetflowLiteMIBObjects,'cnlExporter':cnlExporter,_T:cnlMaxExporterAllowed,'cnlExporterTable':cnlExporterTable,'cnlExporterEntry':cnlExporterEntry,_Q:cnlExporterName,_U:cnlExportAddrType,_V:cnlExportDestinationAddr,_W:cnlExportDestinationUdpPort,_X:cnlExportDestinationUdpLoadShare,_Y:cnlExportSourceAddr,_Z:cnlExportSourceUdpPort,_a:cnlExportVrf,_b:cnlExportTtl,_c:cnlExportCos,_d:cnlExportDscp,_e:cnlExportTemplateTimeout,_f:cnlExportSamplerTableTimeout,_g:cnlExportInterfaceTableTimeout,_h:cnlExportProtocol,_i:cnlPacketExported,_j:cnlExporterStorageType,_k:cnlExporterRowStatus,'cnlSampler':cnlSampler,_l:cnlMaxSamplerAllowed,'cnlSamplerTable':cnlSamplerTable,'cnlSamplerEntry':cnlSamplerEntry,_R:cnlSamplerName,_m:cnlSamplerPacketRate,_n:cnlSamplerPacketSectionSize,_o:cnlSamplerPacketOffset,_p:cnlSamplerStorageType,_q:cnlSamplerRowStatus,'cnlMonitor':cnlMonitor,'cnlIfMonitorTable':cnlIfMonitorTable,'cnlIfMonitorEntry':cnlIfMonitorEntry,_S:cnlIfMonitorSessionName,_r:cnlIfMonitorActiveStatus,_s:cnlIfSamplerName,_t:cnlIfExporterName,_u:cnlIfAveragePacketSize,_v:cnlIfAveragePacketSizeObserved,_w:cnlIfAveragePacketSizeUsed,_x:cnlIfMonitorPktsObserved,_y:cnlIfMonitorPktsExported,_z:cnlIfMonitorPktsDropped,_A0:cnlIfMonitorStorageType,_A1:cnlIfMonitorRowStatus,'ciscoNetflowLiteMIBConform':ciscoNetflowLiteMIBConform,'ciscoNetflowLiteMIBCompliances':ciscoNetflowLiteMIBCompliances,'ciscoNetflowLiteMIBCompliance':ciscoNetflowLiteMIBCompliance,'ciscoNetflowLiteMIBGroups':ciscoNetflowLiteMIBGroups,_A2:cnlExporterInfoGroup,_A3:cnlSamplerInfoGroup,_A4:cnlIfMonitorInfoGroup})