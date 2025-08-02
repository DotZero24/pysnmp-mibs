_M='qtechMplsVPNMgmtRteNextHop'
_L='qtechMplsVPNMgmtRteNHopType'
_K='qtechMplsVPNMgmtRtePolicy'
_J='qtechMplsVPNMgmtRtePfxLen'
_I='qtechMplsVPNMgmtRteDest'
_H='qtechMplsVPNMgmtRteDestType'
_G='Integer32'
_F='InetAddressPrefixLength'
_E='mplsL3VpnVrfName'
_D='MPLS-L3VPN-STD-MIB'
_C='QTECH-MPLS-VPN-MGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_F,'InetAddressType','InetPortNumber')
mplsL3VpnVrfName,=mibBuilder.importSymbols(_D,_E)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp')
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
qtechMplsVPNMgmtMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,122))
if mibBuilder.loadTexts:qtechMplsVPNMgmtMIB.setRevisions(('2013-01-28 00:00',))
_QtechMplsVPNMgmtMIBObjects_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtMIBObjects=_QtechMplsVPNMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,1))
_QtechMplsVPNMgmtVrf_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtVrf=_QtechMplsVPNMgmtVrf_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,1,1))
_QtechMplsVPNMgmtVrfTable_Object=MibTable
qtechMplsVPNMgmtVrfTable=_QtechMplsVPNMgmtVrfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,1,1))
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfTable.setStatus(_A)
_QtechMplsVPNMgmtVrfEntry_Object=MibTableRow
qtechMplsVPNMgmtVrfEntry=_QtechMplsVPNMgmtVrfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,1,1,1))
qtechMplsVPNMgmtVrfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfEntry.setStatus(_A)
_QtechMplsVPNMgmtVrfName_Type=DisplayString
_QtechMplsVPNMgmtVrfName_Object=MibTableColumn
qtechMplsVPNMgmtVrfName=_QtechMplsVPNMgmtVrfName_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,1,1,1,1),_QtechMplsVPNMgmtVrfName_Type())
qtechMplsVPNMgmtVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfName.setStatus(_A)
_QtechMplsVPNMgmtVrfIntfFault_Type=Unsigned32
_QtechMplsVPNMgmtVrfIntfFault_Object=MibTableColumn
qtechMplsVPNMgmtVrfIntfFault=_QtechMplsVPNMgmtVrfIntfFault_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,1,1,1,2),_QtechMplsVPNMgmtVrfIntfFault_Type())
qtechMplsVPNMgmtVrfIntfFault.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfIntfFault.setStatus(_A)
_QtechMplsVPNMgmtVrfVpnId_Type=VPNIdOrZero
_QtechMplsVPNMgmtVrfVpnId_Object=MibTableColumn
qtechMplsVPNMgmtVrfVpnId=_QtechMplsVPNMgmtVrfVpnId_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,1,1,1,3),_QtechMplsVPNMgmtVrfVpnId_Type())
qtechMplsVPNMgmtVrfVpnId.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfVpnId.setStatus(_A)
class _QtechMplsVPNMgmtVrfVpnIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l3vpn',1),('l2vpn',2),('other',3)))
_QtechMplsVPNMgmtVrfVpnIdType_Type.__name__=_G
_QtechMplsVPNMgmtVrfVpnIdType_Object=MibTableColumn
qtechMplsVPNMgmtVrfVpnIdType=_QtechMplsVPNMgmtVrfVpnIdType_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,1,1,1,4),_QtechMplsVPNMgmtVrfVpnIdType_Type())
qtechMplsVPNMgmtVrfVpnIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfVpnIdType.setStatus(_A)
_QtechMplsVPNMgmtRoute_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtRoute=_QtechMplsVPNMgmtRoute_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,1,2))
_QtechMplsVPNMgmtVrfRteTable_Object=MibTable
qtechMplsVPNMgmtVrfRteTable=_QtechMplsVPNMgmtVrfRteTable_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1))
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfRteTable.setStatus(_A)
_QtechMplsVPNMgmtVrfRteEntry_Object=MibTableRow
qtechMplsVPNMgmtVrfRteEntry=_QtechMplsVPNMgmtVrfRteEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1))
qtechMplsVPNMgmtVrfRteEntry.setIndexNames((0,_D,_E),(0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:qtechMplsVPNMgmtVrfRteEntry.setStatus(_A)
_QtechMplsVPNMgmtRteDestType_Type=InetAddressType
_QtechMplsVPNMgmtRteDestType_Object=MibTableColumn
qtechMplsVPNMgmtRteDestType=_QtechMplsVPNMgmtRteDestType_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,1),_QtechMplsVPNMgmtRteDestType_Type())
qtechMplsVPNMgmtRteDestType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRteDestType.setStatus(_A)
_QtechMplsVPNMgmtRteDest_Type=InetAddress
_QtechMplsVPNMgmtRteDest_Object=MibTableColumn
qtechMplsVPNMgmtRteDest=_QtechMplsVPNMgmtRteDest_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,2),_QtechMplsVPNMgmtRteDest_Type())
qtechMplsVPNMgmtRteDest.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRteDest.setStatus(_A)
class _QtechMplsVPNMgmtRtePfxLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_QtechMplsVPNMgmtRtePfxLen_Type.__name__=_F
_QtechMplsVPNMgmtRtePfxLen_Object=MibTableColumn
qtechMplsVPNMgmtRtePfxLen=_QtechMplsVPNMgmtRtePfxLen_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,3),_QtechMplsVPNMgmtRtePfxLen_Type())
qtechMplsVPNMgmtRtePfxLen.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRtePfxLen.setStatus(_A)
_QtechMplsVPNMgmtRtePolicy_Type=ObjectIdentifier
_QtechMplsVPNMgmtRtePolicy_Object=MibTableColumn
qtechMplsVPNMgmtRtePolicy=_QtechMplsVPNMgmtRtePolicy_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,4),_QtechMplsVPNMgmtRtePolicy_Type())
qtechMplsVPNMgmtRtePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRtePolicy.setStatus(_A)
_QtechMplsVPNMgmtRteNHopType_Type=InetAddressType
_QtechMplsVPNMgmtRteNHopType_Object=MibTableColumn
qtechMplsVPNMgmtRteNHopType=_QtechMplsVPNMgmtRteNHopType_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,5),_QtechMplsVPNMgmtRteNHopType_Type())
qtechMplsVPNMgmtRteNHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRteNHopType.setStatus(_A)
_QtechMplsVPNMgmtRteNextHop_Type=InetAddress
_QtechMplsVPNMgmtRteNextHop_Object=MibTableColumn
qtechMplsVPNMgmtRteNextHop=_QtechMplsVPNMgmtRteNextHop_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,6),_QtechMplsVPNMgmtRteNextHop_Type())
qtechMplsVPNMgmtRteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRteNextHop.setStatus(_A)
_QtechMplsVPNMgmtRteDscp_Type=Dscp
_QtechMplsVPNMgmtRteDscp_Object=MibTableColumn
qtechMplsVPNMgmtRteDscp=_QtechMplsVPNMgmtRteDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,7),_QtechMplsVPNMgmtRteDscp_Type())
qtechMplsVPNMgmtRteDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRteDscp.setStatus(_A)
_QtechMplsVPNMgmtRteStorageType_Type=StorageType
_QtechMplsVPNMgmtRteStorageType_Object=MibTableColumn
qtechMplsVPNMgmtRteStorageType=_QtechMplsVPNMgmtRteStorageType_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,2,1,1,8),_QtechMplsVPNMgmtRteStorageType_Type())
qtechMplsVPNMgmtRteStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRteStorageType.setStatus(_A)
_QtechMplsVPNMgmtQos_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtQos=_QtechMplsVPNMgmtQos_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,1,3))
_QtechMplsVPNMgmtQosLSP_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtQosLSP=_QtechMplsVPNMgmtQosLSP_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1))
_QtechMplsVPNMgmtLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtLSPNum_Object=MibScalar
qtechMplsVPNMgmtLSPNum=_QtechMplsVPNMgmtLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,1),_QtechMplsVPNMgmtLSPNum_Type())
qtechMplsVPNMgmtLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtLSPNum.setStatus(_A)
_QtechMplsVPNMgmtBackupLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtBackupLSPNum_Object=MibScalar
qtechMplsVPNMgmtBackupLSPNum=_QtechMplsVPNMgmtBackupLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,2),_QtechMplsVPNMgmtBackupLSPNum_Type())
qtechMplsVPNMgmtBackupLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtBackupLSPNum.setStatus(_A)
_QtechMplsVPNMgmtLDPLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtLDPLSPNum_Object=MibScalar
qtechMplsVPNMgmtLDPLSPNum=_QtechMplsVPNMgmtLDPLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,3),_QtechMplsVPNMgmtLDPLSPNum_Type())
qtechMplsVPNMgmtLDPLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtLDPLSPNum.setStatus(_A)
_QtechMplsVPNMgmtBGPLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtBGPLSPNum_Object=MibScalar
qtechMplsVPNMgmtBGPLSPNum=_QtechMplsVPNMgmtBGPLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,4),_QtechMplsVPNMgmtBGPLSPNum_Type())
qtechMplsVPNMgmtBGPLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtBGPLSPNum.setStatus(_A)
_QtechMplsVPNMgmtStaticLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtStaticLSPNum_Object=MibScalar
qtechMplsVPNMgmtStaticLSPNum=_QtechMplsVPNMgmtStaticLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,5),_QtechMplsVPNMgmtStaticLSPNum_Type())
qtechMplsVPNMgmtStaticLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtStaticLSPNum.setStatus(_A)
_QtechMplsVPNMgmtCRLDPLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtCRLDPLSPNum_Object=MibScalar
qtechMplsVPNMgmtCRLDPLSPNum=_QtechMplsVPNMgmtCRLDPLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,6),_QtechMplsVPNMgmtCRLDPLSPNum_Type())
qtechMplsVPNMgmtCRLDPLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtCRLDPLSPNum.setStatus(_A)
_QtechMplsVPNMgmtRsvpLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtRsvpLSPNum_Object=MibScalar
qtechMplsVPNMgmtRsvpLSPNum=_QtechMplsVPNMgmtRsvpLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,7),_QtechMplsVPNMgmtRsvpLSPNum_Type())
qtechMplsVPNMgmtRsvpLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtRsvpLSPNum.setStatus(_A)
_QtechMplsVPNMgmtBFDLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtBFDLSPNum_Object=MibScalar
qtechMplsVPNMgmtBFDLSPNum=_QtechMplsVPNMgmtBFDLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,8),_QtechMplsVPNMgmtBFDLSPNum_Type())
qtechMplsVPNMgmtBFDLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtBFDLSPNum.setStatus(_A)
_QtechMplsVPNMgmtOAMLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtOAMLSPNum_Object=MibScalar
qtechMplsVPNMgmtOAMLSPNum=_QtechMplsVPNMgmtOAMLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,9),_QtechMplsVPNMgmtOAMLSPNum_Type())
qtechMplsVPNMgmtOAMLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtOAMLSPNum.setStatus(_A)
_QtechMplsVPNMgmtIngressLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtIngressLSPNum_Object=MibScalar
qtechMplsVPNMgmtIngressLSPNum=_QtechMplsVPNMgmtIngressLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,10),_QtechMplsVPNMgmtIngressLSPNum_Type())
qtechMplsVPNMgmtIngressLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtIngressLSPNum.setStatus(_A)
_QtechMplsVPNMgmtTransitLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtTransitLSPNum_Object=MibScalar
qtechMplsVPNMgmtTransitLSPNum=_QtechMplsVPNMgmtTransitLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,11),_QtechMplsVPNMgmtTransitLSPNum_Type())
qtechMplsVPNMgmtTransitLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtTransitLSPNum.setStatus(_A)
_QtechMplsVPNMgmtEgressLSPNum_Type=Unsigned32
_QtechMplsVPNMgmtEgressLSPNum_Object=MibScalar
qtechMplsVPNMgmtEgressLSPNum=_QtechMplsVPNMgmtEgressLSPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,1,12),_QtechMplsVPNMgmtEgressLSPNum_Type())
qtechMplsVPNMgmtEgressLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVPNMgmtEgressLSPNum.setStatus(_A)
_QtechMplsVPNMgmtQosFault_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtQosFault=_QtechMplsVPNMgmtQosFault_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,2))
_QtechMplsLSPFaultBFD_Type=Unsigned32
_QtechMplsLSPFaultBFD_Object=MibScalar
qtechMplsLSPFaultBFD=_QtechMplsLSPFaultBFD_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,2,1),_QtechMplsLSPFaultBFD_Type())
qtechMplsLSPFaultBFD.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsLSPFaultBFD.setStatus(_A)
_QtechMplsLSPFaultOAM_Type=Unsigned32
_QtechMplsLSPFaultOAM_Object=MibScalar
qtechMplsLSPFaultOAM=_QtechMplsLSPFaultOAM_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,2,2),_QtechMplsLSPFaultOAM_Type())
qtechMplsLSPFaultOAM.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsLSPFaultOAM.setStatus(_A)
_QtechMplsVrfFault_Type=Unsigned32
_QtechMplsVrfFault_Object=MibScalar
qtechMplsVrfFault=_QtechMplsVrfFault_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,2,3),_QtechMplsVrfFault_Type())
qtechMplsVrfFault.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsVrfFault.setStatus(_A)
_QtechMplsPWFault_Type=Unsigned32
_QtechMplsPWFault_Object=MibScalar
qtechMplsPWFault=_QtechMplsPWFault_Object((1,3,6,1,4,1,27514,1,1,10,2,122,1,3,2,4),_QtechMplsPWFault_Type())
qtechMplsPWFault.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechMplsPWFault.setStatus(_A)
_QtechMplsVPNMgmtMIBConformance_ObjectIdentity=ObjectIdentity
qtechMplsVPNMgmtMIBConformance=_QtechMplsVPNMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,122,2))
mibBuilder.exportSymbols(_C,**{'qtechMplsVPNMgmtMIB':qtechMplsVPNMgmtMIB,'qtechMplsVPNMgmtMIBObjects':qtechMplsVPNMgmtMIBObjects,'qtechMplsVPNMgmtVrf':qtechMplsVPNMgmtVrf,'qtechMplsVPNMgmtVrfTable':qtechMplsVPNMgmtVrfTable,'qtechMplsVPNMgmtVrfEntry':qtechMplsVPNMgmtVrfEntry,'qtechMplsVPNMgmtVrfName':qtechMplsVPNMgmtVrfName,'qtechMplsVPNMgmtVrfIntfFault':qtechMplsVPNMgmtVrfIntfFault,'qtechMplsVPNMgmtVrfVpnId':qtechMplsVPNMgmtVrfVpnId,'qtechMplsVPNMgmtVrfVpnIdType':qtechMplsVPNMgmtVrfVpnIdType,'qtechMplsVPNMgmtRoute':qtechMplsVPNMgmtRoute,'qtechMplsVPNMgmtVrfRteTable':qtechMplsVPNMgmtVrfRteTable,'qtechMplsVPNMgmtVrfRteEntry':qtechMplsVPNMgmtVrfRteEntry,_H:qtechMplsVPNMgmtRteDestType,_I:qtechMplsVPNMgmtRteDest,_J:qtechMplsVPNMgmtRtePfxLen,_K:qtechMplsVPNMgmtRtePolicy,_L:qtechMplsVPNMgmtRteNHopType,_M:qtechMplsVPNMgmtRteNextHop,'qtechMplsVPNMgmtRteDscp':qtechMplsVPNMgmtRteDscp,'qtechMplsVPNMgmtRteStorageType':qtechMplsVPNMgmtRteStorageType,'qtechMplsVPNMgmtQos':qtechMplsVPNMgmtQos,'qtechMplsVPNMgmtQosLSP':qtechMplsVPNMgmtQosLSP,'qtechMplsVPNMgmtLSPNum':qtechMplsVPNMgmtLSPNum,'qtechMplsVPNMgmtBackupLSPNum':qtechMplsVPNMgmtBackupLSPNum,'qtechMplsVPNMgmtLDPLSPNum':qtechMplsVPNMgmtLDPLSPNum,'qtechMplsVPNMgmtBGPLSPNum':qtechMplsVPNMgmtBGPLSPNum,'qtechMplsVPNMgmtStaticLSPNum':qtechMplsVPNMgmtStaticLSPNum,'qtechMplsVPNMgmtCRLDPLSPNum':qtechMplsVPNMgmtCRLDPLSPNum,'qtechMplsVPNMgmtRsvpLSPNum':qtechMplsVPNMgmtRsvpLSPNum,'qtechMplsVPNMgmtBFDLSPNum':qtechMplsVPNMgmtBFDLSPNum,'qtechMplsVPNMgmtOAMLSPNum':qtechMplsVPNMgmtOAMLSPNum,'qtechMplsVPNMgmtIngressLSPNum':qtechMplsVPNMgmtIngressLSPNum,'qtechMplsVPNMgmtTransitLSPNum':qtechMplsVPNMgmtTransitLSPNum,'qtechMplsVPNMgmtEgressLSPNum':qtechMplsVPNMgmtEgressLSPNum,'qtechMplsVPNMgmtQosFault':qtechMplsVPNMgmtQosFault,'qtechMplsLSPFaultBFD':qtechMplsLSPFaultBFD,'qtechMplsLSPFaultOAM':qtechMplsLSPFaultOAM,'qtechMplsVrfFault':qtechMplsVrfFault,'qtechMplsPWFault':qtechMplsPWFault,'qtechMplsVPNMgmtMIBConformance':qtechMplsVPNMgmtMIBConformance})