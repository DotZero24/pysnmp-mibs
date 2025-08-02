_J='fmpScgPtpGroup'
_I='fmpScgPtpNeighborFPMPOID'
_H='fmpScgPtpProvisionedOpenWaveRemoteTP'
_G='fmpScgPtpMPOAID'
_F='fmpScgPtpProvisionedNeighborTP'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-FMPSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnEnableDisable=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnEnableDisable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fmpScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,53))
if mibBuilder.loadTexts:fmpScgPtpMIB.setRevisions(('2013-10-20 00:00',))
_FmpScgPtpTable_Object=MibTable
fmpScgPtpTable=_FmpScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,53,1))
if mibBuilder.loadTexts:fmpScgPtpTable.setStatus(_A)
_FmpScgPtpEntry_Object=MibTableRow
fmpScgPtpEntry=_FmpScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,53,1,1))
fmpScgPtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fmpScgPtpEntry.setStatus(_A)
_FmpScgPtpProvisionedNeighborTP_Type=DisplayString
_FmpScgPtpProvisionedNeighborTP_Object=MibTableColumn
fmpScgPtpProvisionedNeighborTP=_FmpScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,53,1,1,1),_FmpScgPtpProvisionedNeighborTP_Type())
fmpScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmpScgPtpProvisionedNeighborTP.setStatus(_A)
_FmpScgPtpMPOAID_Type=DisplayString
_FmpScgPtpMPOAID_Object=MibTableColumn
fmpScgPtpMPOAID=_FmpScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,53,1,1,2),_FmpScgPtpMPOAID_Type())
fmpScgPtpMPOAID.setMaxAccess(_C)
if mibBuilder.loadTexts:fmpScgPtpMPOAID.setStatus(_A)
_FmpScgPtpProvisionedOpenWaveRemoteTP_Type=DisplayString
_FmpScgPtpProvisionedOpenWaveRemoteTP_Object=MibTableColumn
fmpScgPtpProvisionedOpenWaveRemoteTP=_FmpScgPtpProvisionedOpenWaveRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,53,1,1,3),_FmpScgPtpProvisionedOpenWaveRemoteTP_Type())
fmpScgPtpProvisionedOpenWaveRemoteTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmpScgPtpProvisionedOpenWaveRemoteTP.setStatus(_A)
_FmpScgPtpNeighborFPMPOID_Type=DisplayString
_FmpScgPtpNeighborFPMPOID_Object=MibTableColumn
fmpScgPtpNeighborFPMPOID=_FmpScgPtpNeighborFPMPOID_Object((1,3,6,1,4,1,21296,2,2,2,2,53,1,1,4),_FmpScgPtpNeighborFPMPOID_Type())
fmpScgPtpNeighborFPMPOID.setMaxAccess(_C)
if mibBuilder.loadTexts:fmpScgPtpNeighborFPMPOID.setStatus(_A)
_FmpScgPtpConformance_ObjectIdentity=ObjectIdentity
fmpScgPtpConformance=_FmpScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,53,3))
_FmpScgPtpCompliances_ObjectIdentity=ObjectIdentity
fmpScgPtpCompliances=_FmpScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,53,3,1))
_FmpScgPtpGroups_ObjectIdentity=ObjectIdentity
fmpScgPtpGroups=_FmpScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,53,3,2))
fmpScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,53,3,2,1))
fmpScgPtpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fmpScgPtpGroup.setStatus(_A)
fmpScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,53,3,1,1))
fmpScgPtpCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:fmpScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmpScgPtpMIB':fmpScgPtpMIB,'fmpScgPtpTable':fmpScgPtpTable,'fmpScgPtpEntry':fmpScgPtpEntry,_F:fmpScgPtpProvisionedNeighborTP,_G:fmpScgPtpMPOAID,_H:fmpScgPtpProvisionedOpenWaveRemoteTP,_I:fmpScgPtpNeighborFPMPOID,'fmpScgPtpConformance':fmpScgPtpConformance,'fmpScgPtpCompliances':fmpScgPtpCompliances,'fmpScgPtpCompliance':fmpScgPtpCompliance,'fmpScgPtpGroups':fmpScgPtpGroups,_J:fmpScgPtpGroup})