_I='lmmPtpGroup'
_H='lmmPtpProvisionedOpenWaveRemoteTP'
_G='lmmPtpTxProvNbrTP'
_F='lmmPtpRxProvNbrTP'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-LMM-MIB'
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
lmmPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,55))
if mibBuilder.loadTexts:lmmPtpMIB.setRevisions(('2013-10-20 00:00',))
_LmmPtpTable_Object=MibTable
lmmPtpTable=_LmmPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,55,1))
if mibBuilder.loadTexts:lmmPtpTable.setStatus(_A)
_LmmPtpEntry_Object=MibTableRow
lmmPtpEntry=_LmmPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,55,1,1))
lmmPtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:lmmPtpEntry.setStatus(_A)
_LmmPtpRxProvNbrTP_Type=DisplayString
_LmmPtpRxProvNbrTP_Object=MibTableColumn
lmmPtpRxProvNbrTP=_LmmPtpRxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,55,1,1,1),_LmmPtpRxProvNbrTP_Type())
lmmPtpRxProvNbrTP.setMaxAccess(_C)
if mibBuilder.loadTexts:lmmPtpRxProvNbrTP.setStatus(_A)
_LmmPtpTxProvNbrTP_Type=DisplayString
_LmmPtpTxProvNbrTP_Object=MibTableColumn
lmmPtpTxProvNbrTP=_LmmPtpTxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,55,1,1,2),_LmmPtpTxProvNbrTP_Type())
lmmPtpTxProvNbrTP.setMaxAccess(_C)
if mibBuilder.loadTexts:lmmPtpTxProvNbrTP.setStatus(_A)
_LmmPtpProvisionedOpenWaveRemoteTP_Type=DisplayString
_LmmPtpProvisionedOpenWaveRemoteTP_Object=MibTableColumn
lmmPtpProvisionedOpenWaveRemoteTP=_LmmPtpProvisionedOpenWaveRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,55,1,1,3),_LmmPtpProvisionedOpenWaveRemoteTP_Type())
lmmPtpProvisionedOpenWaveRemoteTP.setMaxAccess(_C)
if mibBuilder.loadTexts:lmmPtpProvisionedOpenWaveRemoteTP.setStatus(_A)
_LmmPtpConformance_ObjectIdentity=ObjectIdentity
lmmPtpConformance=_LmmPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,55,3))
_LmmPtpCompliances_ObjectIdentity=ObjectIdentity
lmmPtpCompliances=_LmmPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,55,3,1))
_LmmPtpGroups_ObjectIdentity=ObjectIdentity
lmmPtpGroups=_LmmPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,55,3,2))
lmmPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,55,3,2,1))
lmmPtpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:lmmPtpGroup.setStatus(_A)
lmmPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,55,3,1,1))
lmmPtpCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:lmmPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lmmPtpMIB':lmmPtpMIB,'lmmPtpTable':lmmPtpTable,'lmmPtpEntry':lmmPtpEntry,_F:lmmPtpRxProvNbrTP,_G:lmmPtpTxProvNbrTP,_H:lmmPtpProvisionedOpenWaveRemoteTP,'lmmPtpConformance':lmmPtpConformance,'lmmPtpCompliances':lmmPtpCompliances,'lmmPtpCompliance':lmmPtpCompliance,'lmmPtpGroups':lmmPtpGroups,_I:lmmPtpGroup})