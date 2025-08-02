_M='fsMplsVPNMgmtRteNextHop'
_L='fsMplsVPNMgmtRteNHopType'
_K='fsMplsVPNMgmtRtePolicy'
_J='fsMplsVPNMgmtRtePfxLen'
_I='fsMplsVPNMgmtRteDest'
_H='fsMplsVPNMgmtRteDestType'
_G='Integer32'
_F='InetAddressPrefixLength'
_E='mplsL3VpnVrfName'
_D='MPLS-L3VPN-STD-MIB'
_C='FS-MPLS-VPN-MGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_F,'InetAddressType','InetPortNumber')
mplsL3VpnVrfName,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp')
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
fsMplsVPNMgmtMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,122))
if mibBuilder.loadTexts:fsMplsVPNMgmtMIB.setRevisions(('2013-01-28 00:00',))
_FsMplsVPNMgmtMIBObjects_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtMIBObjects=_FsMplsVPNMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,1))
_FsMplsVPNMgmtVrf_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtVrf=_FsMplsVPNMgmtVrf_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,1,1))
_FsMplsVPNMgmtVrfTable_Object=MibTable
fsMplsVPNMgmtVrfTable=_FsMplsVPNMgmtVrfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,1,1))
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfTable.setStatus(_A)
_FsMplsVPNMgmtVrfEntry_Object=MibTableRow
fsMplsVPNMgmtVrfEntry=_FsMplsVPNMgmtVrfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,1,1,1))
fsMplsVPNMgmtVrfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfEntry.setStatus(_A)
_FsMplsVPNMgmtVrfName_Type=DisplayString
_FsMplsVPNMgmtVrfName_Object=MibTableColumn
fsMplsVPNMgmtVrfName=_FsMplsVPNMgmtVrfName_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,1,1,1,1),_FsMplsVPNMgmtVrfName_Type())
fsMplsVPNMgmtVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfName.setStatus(_A)
_FsMplsVPNMgmtVrfIntfFault_Type=Unsigned32
_FsMplsVPNMgmtVrfIntfFault_Object=MibTableColumn
fsMplsVPNMgmtVrfIntfFault=_FsMplsVPNMgmtVrfIntfFault_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,1,1,1,2),_FsMplsVPNMgmtVrfIntfFault_Type())
fsMplsVPNMgmtVrfIntfFault.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfIntfFault.setStatus(_A)
_FsMplsVPNMgmtVrfVpnId_Type=VPNIdOrZero
_FsMplsVPNMgmtVrfVpnId_Object=MibTableColumn
fsMplsVPNMgmtVrfVpnId=_FsMplsVPNMgmtVrfVpnId_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,1,1,1,3),_FsMplsVPNMgmtVrfVpnId_Type())
fsMplsVPNMgmtVrfVpnId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfVpnId.setStatus(_A)
class _FsMplsVPNMgmtVrfVpnIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l3vpn',1),('l2vpn',2),('other',3)))
_FsMplsVPNMgmtVrfVpnIdType_Type.__name__=_G
_FsMplsVPNMgmtVrfVpnIdType_Object=MibTableColumn
fsMplsVPNMgmtVrfVpnIdType=_FsMplsVPNMgmtVrfVpnIdType_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,1,1,1,4),_FsMplsVPNMgmtVrfVpnIdType_Type())
fsMplsVPNMgmtVrfVpnIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfVpnIdType.setStatus(_A)
_FsMplsVPNMgmtRoute_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtRoute=_FsMplsVPNMgmtRoute_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,1,2))
_FsMplsVPNMgmtVrfRteTable_Object=MibTable
fsMplsVPNMgmtVrfRteTable=_FsMplsVPNMgmtVrfRteTable_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1))
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfRteTable.setStatus(_A)
_FsMplsVPNMgmtVrfRteEntry_Object=MibTableRow
fsMplsVPNMgmtVrfRteEntry=_FsMplsVPNMgmtVrfRteEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1))
fsMplsVPNMgmtVrfRteEntry.setIndexNames((0,_D,_E),(0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsMplsVPNMgmtVrfRteEntry.setStatus(_A)
_FsMplsVPNMgmtRteDestType_Type=InetAddressType
_FsMplsVPNMgmtRteDestType_Object=MibTableColumn
fsMplsVPNMgmtRteDestType=_FsMplsVPNMgmtRteDestType_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,1),_FsMplsVPNMgmtRteDestType_Type())
fsMplsVPNMgmtRteDestType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRteDestType.setStatus(_A)
_FsMplsVPNMgmtRteDest_Type=InetAddress
_FsMplsVPNMgmtRteDest_Object=MibTableColumn
fsMplsVPNMgmtRteDest=_FsMplsVPNMgmtRteDest_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,2),_FsMplsVPNMgmtRteDest_Type())
fsMplsVPNMgmtRteDest.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRteDest.setStatus(_A)
class _FsMplsVPNMgmtRtePfxLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsMplsVPNMgmtRtePfxLen_Type.__name__=_F
_FsMplsVPNMgmtRtePfxLen_Object=MibTableColumn
fsMplsVPNMgmtRtePfxLen=_FsMplsVPNMgmtRtePfxLen_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,3),_FsMplsVPNMgmtRtePfxLen_Type())
fsMplsVPNMgmtRtePfxLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRtePfxLen.setStatus(_A)
_FsMplsVPNMgmtRtePolicy_Type=ObjectIdentifier
_FsMplsVPNMgmtRtePolicy_Object=MibTableColumn
fsMplsVPNMgmtRtePolicy=_FsMplsVPNMgmtRtePolicy_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,4),_FsMplsVPNMgmtRtePolicy_Type())
fsMplsVPNMgmtRtePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRtePolicy.setStatus(_A)
_FsMplsVPNMgmtRteNHopType_Type=InetAddressType
_FsMplsVPNMgmtRteNHopType_Object=MibTableColumn
fsMplsVPNMgmtRteNHopType=_FsMplsVPNMgmtRteNHopType_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,5),_FsMplsVPNMgmtRteNHopType_Type())
fsMplsVPNMgmtRteNHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRteNHopType.setStatus(_A)
_FsMplsVPNMgmtRteNextHop_Type=InetAddress
_FsMplsVPNMgmtRteNextHop_Object=MibTableColumn
fsMplsVPNMgmtRteNextHop=_FsMplsVPNMgmtRteNextHop_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,6),_FsMplsVPNMgmtRteNextHop_Type())
fsMplsVPNMgmtRteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRteNextHop.setStatus(_A)
_FsMplsVPNMgmtRteDscp_Type=Dscp
_FsMplsVPNMgmtRteDscp_Object=MibTableColumn
fsMplsVPNMgmtRteDscp=_FsMplsVPNMgmtRteDscp_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,7),_FsMplsVPNMgmtRteDscp_Type())
fsMplsVPNMgmtRteDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRteDscp.setStatus(_A)
_FsMplsVPNMgmtRteStorageType_Type=StorageType
_FsMplsVPNMgmtRteStorageType_Object=MibTableColumn
fsMplsVPNMgmtRteStorageType=_FsMplsVPNMgmtRteStorageType_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,2,1,1,8),_FsMplsVPNMgmtRteStorageType_Type())
fsMplsVPNMgmtRteStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRteStorageType.setStatus(_A)
_FsMplsVPNMgmtQos_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtQos=_FsMplsVPNMgmtQos_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,1,3))
_FsMplsVPNMgmtQosLSP_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtQosLSP=_FsMplsVPNMgmtQosLSP_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1))
_FsMplsVPNMgmtLSPNum_Type=Unsigned32
_FsMplsVPNMgmtLSPNum_Object=MibScalar
fsMplsVPNMgmtLSPNum=_FsMplsVPNMgmtLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,1),_FsMplsVPNMgmtLSPNum_Type())
fsMplsVPNMgmtLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtLSPNum.setStatus(_A)
_FsMplsVPNMgmtBackupLSPNum_Type=Unsigned32
_FsMplsVPNMgmtBackupLSPNum_Object=MibScalar
fsMplsVPNMgmtBackupLSPNum=_FsMplsVPNMgmtBackupLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,2),_FsMplsVPNMgmtBackupLSPNum_Type())
fsMplsVPNMgmtBackupLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtBackupLSPNum.setStatus(_A)
_FsMplsVPNMgmtLDPLSPNum_Type=Unsigned32
_FsMplsVPNMgmtLDPLSPNum_Object=MibScalar
fsMplsVPNMgmtLDPLSPNum=_FsMplsVPNMgmtLDPLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,3),_FsMplsVPNMgmtLDPLSPNum_Type())
fsMplsVPNMgmtLDPLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtLDPLSPNum.setStatus(_A)
_FsMplsVPNMgmtBGPLSPNum_Type=Unsigned32
_FsMplsVPNMgmtBGPLSPNum_Object=MibScalar
fsMplsVPNMgmtBGPLSPNum=_FsMplsVPNMgmtBGPLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,4),_FsMplsVPNMgmtBGPLSPNum_Type())
fsMplsVPNMgmtBGPLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtBGPLSPNum.setStatus(_A)
_FsMplsVPNMgmtStaticLSPNum_Type=Unsigned32
_FsMplsVPNMgmtStaticLSPNum_Object=MibScalar
fsMplsVPNMgmtStaticLSPNum=_FsMplsVPNMgmtStaticLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,5),_FsMplsVPNMgmtStaticLSPNum_Type())
fsMplsVPNMgmtStaticLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtStaticLSPNum.setStatus(_A)
_FsMplsVPNMgmtCRLDPLSPNum_Type=Unsigned32
_FsMplsVPNMgmtCRLDPLSPNum_Object=MibScalar
fsMplsVPNMgmtCRLDPLSPNum=_FsMplsVPNMgmtCRLDPLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,6),_FsMplsVPNMgmtCRLDPLSPNum_Type())
fsMplsVPNMgmtCRLDPLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtCRLDPLSPNum.setStatus(_A)
_FsMplsVPNMgmtRsvpLSPNum_Type=Unsigned32
_FsMplsVPNMgmtRsvpLSPNum_Object=MibScalar
fsMplsVPNMgmtRsvpLSPNum=_FsMplsVPNMgmtRsvpLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,7),_FsMplsVPNMgmtRsvpLSPNum_Type())
fsMplsVPNMgmtRsvpLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtRsvpLSPNum.setStatus(_A)
_FsMplsVPNMgmtBFDLSPNum_Type=Unsigned32
_FsMplsVPNMgmtBFDLSPNum_Object=MibScalar
fsMplsVPNMgmtBFDLSPNum=_FsMplsVPNMgmtBFDLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,8),_FsMplsVPNMgmtBFDLSPNum_Type())
fsMplsVPNMgmtBFDLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtBFDLSPNum.setStatus(_A)
_FsMplsVPNMgmtOAMLSPNum_Type=Unsigned32
_FsMplsVPNMgmtOAMLSPNum_Object=MibScalar
fsMplsVPNMgmtOAMLSPNum=_FsMplsVPNMgmtOAMLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,9),_FsMplsVPNMgmtOAMLSPNum_Type())
fsMplsVPNMgmtOAMLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtOAMLSPNum.setStatus(_A)
_FsMplsVPNMgmtIngressLSPNum_Type=Unsigned32
_FsMplsVPNMgmtIngressLSPNum_Object=MibScalar
fsMplsVPNMgmtIngressLSPNum=_FsMplsVPNMgmtIngressLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,10),_FsMplsVPNMgmtIngressLSPNum_Type())
fsMplsVPNMgmtIngressLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtIngressLSPNum.setStatus(_A)
_FsMplsVPNMgmtTransitLSPNum_Type=Unsigned32
_FsMplsVPNMgmtTransitLSPNum_Object=MibScalar
fsMplsVPNMgmtTransitLSPNum=_FsMplsVPNMgmtTransitLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,11),_FsMplsVPNMgmtTransitLSPNum_Type())
fsMplsVPNMgmtTransitLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtTransitLSPNum.setStatus(_A)
_FsMplsVPNMgmtEgressLSPNum_Type=Unsigned32
_FsMplsVPNMgmtEgressLSPNum_Object=MibScalar
fsMplsVPNMgmtEgressLSPNum=_FsMplsVPNMgmtEgressLSPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,1,12),_FsMplsVPNMgmtEgressLSPNum_Type())
fsMplsVPNMgmtEgressLSPNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVPNMgmtEgressLSPNum.setStatus(_A)
_FsMplsVPNMgmtQosFault_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtQosFault=_FsMplsVPNMgmtQosFault_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,2))
_FsMplsLSPFaultBFD_Type=Unsigned32
_FsMplsLSPFaultBFD_Object=MibScalar
fsMplsLSPFaultBFD=_FsMplsLSPFaultBFD_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,2,1),_FsMplsLSPFaultBFD_Type())
fsMplsLSPFaultBFD.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsLSPFaultBFD.setStatus(_A)
_FsMplsLSPFaultOAM_Type=Unsigned32
_FsMplsLSPFaultOAM_Object=MibScalar
fsMplsLSPFaultOAM=_FsMplsLSPFaultOAM_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,2,2),_FsMplsLSPFaultOAM_Type())
fsMplsLSPFaultOAM.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsLSPFaultOAM.setStatus(_A)
_FsMplsVrfFault_Type=Unsigned32
_FsMplsVrfFault_Object=MibScalar
fsMplsVrfFault=_FsMplsVrfFault_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,2,3),_FsMplsVrfFault_Type())
fsMplsVrfFault.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsVrfFault.setStatus(_A)
_FsMplsPWFault_Type=Unsigned32
_FsMplsPWFault_Object=MibScalar
fsMplsPWFault=_FsMplsPWFault_Object((1,3,6,1,4,1,52642,1,1,10,2,122,1,3,2,4),_FsMplsPWFault_Type())
fsMplsPWFault.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsPWFault.setStatus(_A)
_FsMplsVPNMgmtMIBConformance_ObjectIdentity=ObjectIdentity
fsMplsVPNMgmtMIBConformance=_FsMplsVPNMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,122,2))
mibBuilder.exportSymbols(_C,**{'fsMplsVPNMgmtMIB':fsMplsVPNMgmtMIB,'fsMplsVPNMgmtMIBObjects':fsMplsVPNMgmtMIBObjects,'fsMplsVPNMgmtVrf':fsMplsVPNMgmtVrf,'fsMplsVPNMgmtVrfTable':fsMplsVPNMgmtVrfTable,'fsMplsVPNMgmtVrfEntry':fsMplsVPNMgmtVrfEntry,'fsMplsVPNMgmtVrfName':fsMplsVPNMgmtVrfName,'fsMplsVPNMgmtVrfIntfFault':fsMplsVPNMgmtVrfIntfFault,'fsMplsVPNMgmtVrfVpnId':fsMplsVPNMgmtVrfVpnId,'fsMplsVPNMgmtVrfVpnIdType':fsMplsVPNMgmtVrfVpnIdType,'fsMplsVPNMgmtRoute':fsMplsVPNMgmtRoute,'fsMplsVPNMgmtVrfRteTable':fsMplsVPNMgmtVrfRteTable,'fsMplsVPNMgmtVrfRteEntry':fsMplsVPNMgmtVrfRteEntry,_H:fsMplsVPNMgmtRteDestType,_I:fsMplsVPNMgmtRteDest,_J:fsMplsVPNMgmtRtePfxLen,_K:fsMplsVPNMgmtRtePolicy,_L:fsMplsVPNMgmtRteNHopType,_M:fsMplsVPNMgmtRteNextHop,'fsMplsVPNMgmtRteDscp':fsMplsVPNMgmtRteDscp,'fsMplsVPNMgmtRteStorageType':fsMplsVPNMgmtRteStorageType,'fsMplsVPNMgmtQos':fsMplsVPNMgmtQos,'fsMplsVPNMgmtQosLSP':fsMplsVPNMgmtQosLSP,'fsMplsVPNMgmtLSPNum':fsMplsVPNMgmtLSPNum,'fsMplsVPNMgmtBackupLSPNum':fsMplsVPNMgmtBackupLSPNum,'fsMplsVPNMgmtLDPLSPNum':fsMplsVPNMgmtLDPLSPNum,'fsMplsVPNMgmtBGPLSPNum':fsMplsVPNMgmtBGPLSPNum,'fsMplsVPNMgmtStaticLSPNum':fsMplsVPNMgmtStaticLSPNum,'fsMplsVPNMgmtCRLDPLSPNum':fsMplsVPNMgmtCRLDPLSPNum,'fsMplsVPNMgmtRsvpLSPNum':fsMplsVPNMgmtRsvpLSPNum,'fsMplsVPNMgmtBFDLSPNum':fsMplsVPNMgmtBFDLSPNum,'fsMplsVPNMgmtOAMLSPNum':fsMplsVPNMgmtOAMLSPNum,'fsMplsVPNMgmtIngressLSPNum':fsMplsVPNMgmtIngressLSPNum,'fsMplsVPNMgmtTransitLSPNum':fsMplsVPNMgmtTransitLSPNum,'fsMplsVPNMgmtEgressLSPNum':fsMplsVPNMgmtEgressLSPNum,'fsMplsVPNMgmtQosFault':fsMplsVPNMgmtQosFault,'fsMplsLSPFaultBFD':fsMplsLSPFaultBFD,'fsMplsLSPFaultOAM':fsMplsLSPFaultOAM,'fsMplsVrfFault':fsMplsVrfFault,'fsMplsPWFault':fsMplsPWFault,'fsMplsVPNMgmtMIBConformance':fsMplsVPNMgmtMIBConformance})