_U='eapName'
_T='vlanIdx'
_S='portsName'
_R='full1000'
_Q='full100'
_P='half100'
_O='full10'
_N='half10'
_M='portsStatusName'
_L='disable'
_K='linksName'
_J='disconnected'
_I='linkStatusLinkName'
_H='MxEnableState'
_G='OctetString'
_F='Unsigned32'
_E='MX-ETH-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_H,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ethMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2400))
_EthMIBObjects_ObjectIdentity=ObjectIdentity
ethMIBObjects=_EthMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2400,1))
_LinkStatusTable_Object=MibTable
linkStatusTable=_LinkStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,25))
if mibBuilder.loadTexts:linkStatusTable.setStatus(_A)
_LinkStatusEntry_Object=MibTableRow
linkStatusEntry=_LinkStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,25,1))
linkStatusEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:linkStatusEntry.setStatus(_A)
_LinkStatusLinkName_Type=OctetString
_LinkStatusLinkName_Object=MibTableColumn
linkStatusLinkName=_LinkStatusLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,25,1,100),_LinkStatusLinkName_Type())
linkStatusLinkName.setMaxAccess(_B)
if mibBuilder.loadTexts:linkStatusLinkName.setStatus(_A)
_LinkStatusLinkType_Type=OctetString
_LinkStatusLinkType_Object=MibTableColumn
linkStatusLinkType=_LinkStatusLinkType_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,25,1,200),_LinkStatusLinkType_Type())
linkStatusLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkStatusLinkType.setStatus(_A)
class _LinkStatusLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_J,100),('up',200)))
_LinkStatusLinkState_Type.__name__=_D
_LinkStatusLinkState_Object=MibTableColumn
linkStatusLinkState=_LinkStatusLinkState_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,25,1,300),_LinkStatusLinkState_Type())
linkStatusLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:linkStatusLinkState.setStatus(_A)
_LinksTable_Object=MibTable
linksTable=_LinksTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,50))
if mibBuilder.loadTexts:linksTable.setStatus(_A)
_LinksEntry_Object=MibTableRow
linksEntry=_LinksEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,50,1))
linksEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linksEntry.setStatus(_A)
_LinksName_Type=OctetString
_LinksName_Object=MibTableColumn
linksName=_LinksName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,50,1,100),_LinksName_Type())
linksName.setMaxAccess(_B)
if mibBuilder.loadTexts:linksName.setStatus(_A)
class _LinksMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(576,1500))
_LinksMtu_Type.__name__=_F
_LinksMtu_Object=MibTableColumn
linksMtu=_LinksMtu_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,50,1,200),_LinksMtu_Type())
linksMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:linksMtu.setStatus(_A)
class _LinksIeee8021XAuthentication_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_L,100),('enable',200)))
_LinksIeee8021XAuthentication_Type.__name__=_D
_LinksIeee8021XAuthentication_Object=MibTableColumn
linksIeee8021XAuthentication=_LinksIeee8021XAuthentication_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,50,1,300),_LinksIeee8021XAuthentication_Type())
linksIeee8021XAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:linksIeee8021XAuthentication.setStatus(_A)
class _LinksVirtualSwitch_Type(MxEnableState):defaultValue=0
_LinksVirtualSwitch_Type.__name__=_H
_LinksVirtualSwitch_Object=MibTableColumn
linksVirtualSwitch=_LinksVirtualSwitch_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,50,1,400),_LinksVirtualSwitch_Type())
linksVirtualSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:linksVirtualSwitch.setStatus(_A)
_PortsStatusTable_Object=MibTable
portsStatusTable=_PortsStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,100))
if mibBuilder.loadTexts:portsStatusTable.setStatus(_A)
_PortsStatusEntry_Object=MibTableRow
portsStatusEntry=_PortsStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,100,1))
portsStatusEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:portsStatusEntry.setStatus(_A)
_PortsStatusName_Type=OctetString
_PortsStatusName_Object=MibTableColumn
portsStatusName=_PortsStatusName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,100,1,100),_PortsStatusName_Type())
portsStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:portsStatusName.setStatus(_A)
_PortsStatusLinkName_Type=OctetString
_PortsStatusLinkName_Object=MibTableColumn
portsStatusLinkName=_PortsStatusLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,100,1,200),_PortsStatusLinkName_Type())
portsStatusLinkName.setMaxAccess(_B)
if mibBuilder.loadTexts:portsStatusLinkName.setStatus(_A)
class _PortsStatusConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_J,0),(_N,100),(_O,200),(_P,300),(_Q,400),(_R,500)))
_PortsStatusConnection_Type.__name__=_D
_PortsStatusConnection_Object=MibTableColumn
portsStatusConnection=_PortsStatusConnection_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,100,1,300),_PortsStatusConnection_Type())
portsStatusConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:portsStatusConnection.setStatus(_A)
_PortsTable_Object=MibTable
portsTable=_PortsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,200))
if mibBuilder.loadTexts:portsTable.setStatus(_A)
_PortsEntry_Object=MibTableRow
portsEntry=_PortsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,200,1))
portsEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:portsEntry.setStatus(_A)
_PortsName_Type=OctetString
_PortsName_Object=MibTableColumn
portsName=_PortsName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,200,1,100),_PortsName_Type())
portsName.setMaxAccess(_B)
if mibBuilder.loadTexts:portsName.setStatus(_A)
class _PortsSpeed_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*(('auto',100),(_N,200),(_O,300),(_P,400),(_Q,500),(_R,600)))
_PortsSpeed_Type.__name__=_D
_PortsSpeed_Object=MibTableColumn
portsSpeed=_PortsSpeed_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,200,1,200),_PortsSpeed_Type())
portsSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portsSpeed.setStatus(_A)
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1))
vlanEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
_VlanIdx_Type=Unsigned32
_VlanIdx_Object=MibTableColumn
vlanIdx=_VlanIdx_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1,50),_VlanIdx_Type())
vlanIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanIdx.setStatus(_A)
class _VlanLinkName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_VlanLinkName_Type.__name__=_G
_VlanLinkName_Object=MibTableColumn
vlanLinkName=_VlanLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1,100),_VlanLinkName_Type())
vlanLinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanLinkName.setStatus(_A)
class _VlanVlanId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanVlanId_Type.__name__=_F
_VlanVlanId_Object=MibTableColumn
vlanVlanId=_VlanVlanId_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1,200),_VlanVlanId_Type())
vlanVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVlanId.setStatus(_A)
class _VlanDefaultUserPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanDefaultUserPriority_Type.__name__=_F
_VlanDefaultUserPriority_Object=MibTableColumn
vlanDefaultUserPriority=_VlanDefaultUserPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1,300),_VlanDefaultUserPriority_Type())
vlanDefaultUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDefaultUserPriority.setStatus(_A)
class _VlanConfigStatus_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('validConfig',100),('invalidLinkName',200),('invalidVlanId',300),('duplicateLinkVlanId',400)))
_VlanConfigStatus_Type.__name__=_D
_VlanConfigStatus_Object=MibTableColumn
vlanConfigStatus=_VlanConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1,350),_VlanConfigStatus_Type())
vlanConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanConfigStatus.setStatus(_A)
class _VlanDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('delete',10)))
_VlanDelete_Type.__name__=_D
_VlanDelete_Object=MibTableColumn
vlanDelete=_VlanDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,300,1,400),_VlanDelete_Type())
vlanDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDelete.setStatus(_A)
_EapGroup_ObjectIdentity=ObjectIdentity
eapGroup=_EapGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000))
_EapTable_Object=MibTable
eapTable=_EapTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000,100))
if mibBuilder.loadTexts:eapTable.setStatus(_A)
_EapEntry_Object=MibTableRow
eapEntry=_EapEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000,100,1))
eapEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:eapEntry.setStatus(_A)
_EapName_Type=OctetString
_EapName_Object=MibTableColumn
eapName=_EapName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000,100,1,100),_EapName_Type())
eapName.setMaxAccess(_B)
if mibBuilder.loadTexts:eapName.setStatus(_A)
class _EapUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EapUsername_Type.__name__=_G
_EapUsername_Object=MibTableColumn
eapUsername=_EapUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000,100,1,200),_EapUsername_Type())
eapUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:eapUsername.setStatus(_A)
class _EapCertificateValidation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('noValidation',100),('trustedAndValid',200)))
_EapCertificateValidation_Type.__name__=_D
_EapCertificateValidation_Object=MibTableColumn
eapCertificateValidation=_EapCertificateValidation_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000,100,1,300),_EapCertificateValidation_Type())
eapCertificateValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:eapCertificateValidation.setStatus(_A)
class _Ieee8021XVersion_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('ieee8021X2001',100),('ieee8021X2004',200)))
_Ieee8021XVersion_Type.__name__=_D
_Ieee8021XVersion_Object=MibScalar
ieee8021XVersion=_Ieee8021XVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,10000,200),_Ieee8021XVersion_Type())
ieee8021XVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021XVersion.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_L,0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,2400,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ethMIB':ethMIB,'ethMIBObjects':ethMIBObjects,'linkStatusTable':linkStatusTable,'linkStatusEntry':linkStatusEntry,_I:linkStatusLinkName,'linkStatusLinkType':linkStatusLinkType,'linkStatusLinkState':linkStatusLinkState,'linksTable':linksTable,'linksEntry':linksEntry,_K:linksName,'linksMtu':linksMtu,'linksIeee8021XAuthentication':linksIeee8021XAuthentication,'linksVirtualSwitch':linksVirtualSwitch,'portsStatusTable':portsStatusTable,'portsStatusEntry':portsStatusEntry,_M:portsStatusName,'portsStatusLinkName':portsStatusLinkName,'portsStatusConnection':portsStatusConnection,'portsTable':portsTable,'portsEntry':portsEntry,_S:portsName,'portsSpeed':portsSpeed,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_T:vlanIdx,'vlanLinkName':vlanLinkName,'vlanVlanId':vlanVlanId,'vlanDefaultUserPriority':vlanDefaultUserPriority,'vlanConfigStatus':vlanConfigStatus,'vlanDelete':vlanDelete,'eapGroup':eapGroup,'eapTable':eapTable,'eapEntry':eapEntry,_U:eapName,'eapUsername':eapUsername,'eapCertificateValidation':eapCertificateValidation,'ieee8021XVersion':ieee8021XVersion,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})