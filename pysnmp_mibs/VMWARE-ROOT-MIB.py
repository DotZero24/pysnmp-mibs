_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmware=ModuleIdentity((1,3,6,1,4,1,6876))
if mibBuilder.loadTexts:vmware.setRevisions(('2021-05-17 00:00','2018-08-30 00:00','2017-10-30 00:00','2017-06-07 00:00','2016-11-03 00:00','2016-01-02 20:00','2010-04-02 00:00','2007-07-30 00:00'))
_VmwNotifications_ObjectIdentity=ObjectIdentity
vmwNotifications=_VmwNotifications_ObjectIdentity((1,3,6,1,4,1,6876,0))
if mibBuilder.loadTexts:vmwNotifications.setStatus(_A)
_VmwSystem_ObjectIdentity=ObjectIdentity
vmwSystem=_VmwSystem_ObjectIdentity((1,3,6,1,4,1,6876,1))
if mibBuilder.loadTexts:vmwSystem.setStatus(_A)
_VmwVirtMachines_ObjectIdentity=ObjectIdentity
vmwVirtMachines=_VmwVirtMachines_ObjectIdentity((1,3,6,1,4,1,6876,2))
if mibBuilder.loadTexts:vmwVirtMachines.setStatus(_A)
_VmwResources_ObjectIdentity=ObjectIdentity
vmwResources=_VmwResources_ObjectIdentity((1,3,6,1,4,1,6876,3))
if mibBuilder.loadTexts:vmwResources.setStatus(_A)
_VmwProductSpecific_ObjectIdentity=ObjectIdentity
vmwProductSpecific=_VmwProductSpecific_ObjectIdentity((1,3,6,1,4,1,6876,4))
if mibBuilder.loadTexts:vmwProductSpecific.setStatus(_A)
_VmwLdap_ObjectIdentity=ObjectIdentity
vmwLdap=_VmwLdap_ObjectIdentity((1,3,6,1,4,1,6876,40))
if mibBuilder.loadTexts:vmwLdap.setStatus(_A)
_VmwTraps_ObjectIdentity=ObjectIdentity
vmwTraps=_VmwTraps_ObjectIdentity((1,3,6,1,4,1,6876,50))
if mibBuilder.loadTexts:vmwTraps.setStatus(_A)
_VmwSRM_ObjectIdentity=ObjectIdentity
vmwSRM=_VmwSRM_ObjectIdentity((1,3,6,1,4,1,6876,51))
if mibBuilder.loadTexts:vmwSRM.setStatus(_A)
_VmwVCHA_ObjectIdentity=ObjectIdentity
vmwVCHA=_VmwVCHA_ObjectIdentity((1,3,6,1,4,1,6876,53))
if mibBuilder.loadTexts:vmwVCHA.setStatus(_A)
_VmwVmon_ObjectIdentity=ObjectIdentity
vmwVmon=_VmwVmon_ObjectIdentity((1,3,6,1,4,1,6876,55))
if mibBuilder.loadTexts:vmwVmon.setStatus(_A)
_VmwOID_ObjectIdentity=ObjectIdentity
vmwOID=_VmwOID_ObjectIdentity((1,3,6,1,4,1,6876,60))
if mibBuilder.loadTexts:vmwOID.setStatus('deprecated')
_VmwareAgentCapabilities_ObjectIdentity=ObjectIdentity
vmwareAgentCapabilities=_VmwareAgentCapabilities_ObjectIdentity((1,3,6,1,4,1,6876,70))
if mibBuilder.loadTexts:vmwareAgentCapabilities.setStatus(_A)
_VmwNsxManager_ObjectIdentity=ObjectIdentity
vmwNsxManager=_VmwNsxManager_ObjectIdentity((1,3,6,1,4,1,6876,90))
if mibBuilder.loadTexts:vmwNsxManager.setStatus(_A)
_VmwNetworkInsight_ObjectIdentity=ObjectIdentity
vmwNetworkInsight=_VmwNetworkInsight_ObjectIdentity((1,3,6,1,4,1,6876,100))
if mibBuilder.loadTexts:vmwNetworkInsight.setStatus(_A)
_VmwHCX_ObjectIdentity=ObjectIdentity
vmwHCX=_VmwHCX_ObjectIdentity((1,3,6,1,4,1,6876,110))
if mibBuilder.loadTexts:vmwHCX.setStatus(_A)
_VmwNSXsys_ObjectIdentity=ObjectIdentity
vmwNSXsys=_VmwNSXsys_ObjectIdentity((1,3,6,1,4,1,6876,120))
if mibBuilder.loadTexts:vmwNSXsys.setStatus(_A)
_VmwPerAppTunnel_ObjectIdentity=ObjectIdentity
vmwPerAppTunnel=_VmwPerAppTunnel_ObjectIdentity((1,3,6,1,4,1,6876,130))
if mibBuilder.loadTexts:vmwPerAppTunnel.setStatus(_A)
_VmwHzecc_ObjectIdentity=ObjectIdentity
vmwHzecc=_VmwHzecc_ObjectIdentity((1,3,6,1,4,1,6876,140))
if mibBuilder.loadTexts:vmwHzecc.setStatus(_A)
_VmwHorizonv2_ObjectIdentity=ObjectIdentity
vmwHorizonv2=_VmwHorizonv2_ObjectIdentity((1,3,6,1,4,1,6876,150))
if mibBuilder.loadTexts:vmwHorizonv2.setStatus(_A)
_VmwExperimental_ObjectIdentity=ObjectIdentity
vmwExperimental=_VmwExperimental_ObjectIdentity((1,3,6,1,4,1,6876,700))
if mibBuilder.loadTexts:vmwExperimental.setStatus(_A)
_VmwDocumentation_ObjectIdentity=ObjectIdentity
vmwDocumentation=_VmwDocumentation_ObjectIdentity((1,3,6,1,4,1,6876,750))
if mibBuilder.loadTexts:vmwDocumentation.setStatus(_A)
_VmwObsolete_ObjectIdentity=ObjectIdentity
vmwObsolete=_VmwObsolete_ObjectIdentity((1,3,6,1,4,1,6876,800))
if mibBuilder.loadTexts:vmwObsolete.setStatus(_A)
mibBuilder.exportSymbols('VMWARE-ROOT-MIB',**{'vmware':vmware,'vmwNotifications':vmwNotifications,'vmwSystem':vmwSystem,'vmwVirtMachines':vmwVirtMachines,'vmwResources':vmwResources,'vmwProductSpecific':vmwProductSpecific,'vmwLdap':vmwLdap,'vmwTraps':vmwTraps,'vmwSRM':vmwSRM,'vmwVCHA':vmwVCHA,'vmwVmon':vmwVmon,'vmwOID':vmwOID,'vmwareAgentCapabilities':vmwareAgentCapabilities,'vmwNsxManager':vmwNsxManager,'vmwNetworkInsight':vmwNetworkInsight,'vmwHCX':vmwHCX,'vmwNSXsys':vmwNSXsys,'vmwPerAppTunnel':vmwPerAppTunnel,'vmwHzecc':vmwHzecc,'vmwHorizonv2':vmwHorizonv2,'vmwExperimental':vmwExperimental,'vmwDocumentation':vmwDocumentation,'vmwObsolete':vmwObsolete})