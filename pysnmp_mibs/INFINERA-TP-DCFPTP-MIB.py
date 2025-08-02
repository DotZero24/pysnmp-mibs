_Q='dcfPtpGroup'
_P='dcfPtpPmHistStatsEnable'
_O='dcfPtpDcfLossReporting'
_N='dcfPtpExpectedDispersion'
_M='dcfPtpExpectedDcfLoss'
_L='dcfPtpDcmType'
_K='enabled'
_J='disabled'
_I='InfnDcmType'
_H='FloatTenths'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='INFINERA-TP-DCFPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnDcmType=mibBuilder.importSymbols('INFINERA-TC-MIB',_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dcfPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,5))
if mibBuilder.loadTexts:dcfPtpMIB.setRevisions(('2008-10-20 00:00',))
_DcfPtpTable_Object=MibTable
dcfPtpTable=_DcfPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1))
if mibBuilder.loadTexts:dcfPtpTable.setStatus(_A)
_DcfPtpEntry_Object=MibTableRow
dcfPtpEntry=_DcfPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1))
dcfPtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dcfPtpEntry.setStatus(_A)
class _DcfPtpDcmType_Type(InfnDcmType):defaultValue=25
_DcfPtpDcmType_Type.__name__=_I
_DcfPtpDcmType_Object=MibTableColumn
dcfPtpDcmType=_DcfPtpDcmType_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1,1),_DcfPtpDcmType_Type())
dcfPtpDcmType.setMaxAccess(_D)
if mibBuilder.loadTexts:dcfPtpDcmType.setStatus(_A)
class _DcfPtpExpectedDcfLoss_Type(FloatTenths):defaultValue=0
_DcfPtpExpectedDcfLoss_Type.__name__=_H
_DcfPtpExpectedDcfLoss_Object=MibTableColumn
dcfPtpExpectedDcfLoss=_DcfPtpExpectedDcfLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1,2),_DcfPtpExpectedDcfLoss_Type())
dcfPtpExpectedDcfLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:dcfPtpExpectedDcfLoss.setStatus(_A)
if mibBuilder.loadTexts:dcfPtpExpectedDcfLoss.setUnits('0.1 dB')
class _DcfPtpExpectedDispersion_Type(Integer32):defaultValue=0
_DcfPtpExpectedDispersion_Type.__name__=_C
_DcfPtpExpectedDispersion_Object=MibTableColumn
dcfPtpExpectedDispersion=_DcfPtpExpectedDispersion_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1,3),_DcfPtpExpectedDispersion_Type())
dcfPtpExpectedDispersion.setMaxAccess(_E)
if mibBuilder.loadTexts:dcfPtpExpectedDispersion.setStatus(_A)
if mibBuilder.loadTexts:dcfPtpExpectedDispersion.setUnits('100 ps/nm')
class _DcfPtpDcfLossReporting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_DcfPtpDcfLossReporting_Type.__name__=_C
_DcfPtpDcfLossReporting_Object=MibTableColumn
dcfPtpDcfLossReporting=_DcfPtpDcfLossReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1,4),_DcfPtpDcfLossReporting_Type())
dcfPtpDcfLossReporting.setMaxAccess(_D)
if mibBuilder.loadTexts:dcfPtpDcfLossReporting.setStatus(_A)
class _DcfPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_DcfPtpPmHistStatsEnable_Type.__name__=_C
_DcfPtpPmHistStatsEnable_Object=MibTableColumn
dcfPtpPmHistStatsEnable=_DcfPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1,5),_DcfPtpPmHistStatsEnable_Type())
dcfPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dcfPtpPmHistStatsEnable.setStatus(_A)
_DcfPtpProvisionedRemoteTP_Type=DisplayString
_DcfPtpProvisionedRemoteTP_Object=MibTableColumn
dcfPtpProvisionedRemoteTP=_DcfPtpProvisionedRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,5,1,1,6),_DcfPtpProvisionedRemoteTP_Type())
dcfPtpProvisionedRemoteTP.setMaxAccess(_E)
if mibBuilder.loadTexts:dcfPtpProvisionedRemoteTP.setStatus(_A)
_DcfPtpConformance_ObjectIdentity=ObjectIdentity
dcfPtpConformance=_DcfPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,5,3))
_DcfPtpCompliances_ObjectIdentity=ObjectIdentity
dcfPtpCompliances=_DcfPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,5,3,1))
_DcfPtpGroups_ObjectIdentity=ObjectIdentity
dcfPtpGroups=_DcfPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,5,3,2))
dcfPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,5,3,2,1))
dcfPtpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dcfPtpGroup.setStatus(_A)
dcfPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,5,3,1,1))
dcfPtpCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:dcfPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dcfPtpMIB':dcfPtpMIB,'dcfPtpTable':dcfPtpTable,'dcfPtpEntry':dcfPtpEntry,_L:dcfPtpDcmType,_M:dcfPtpExpectedDcfLoss,_N:dcfPtpExpectedDispersion,_O:dcfPtpDcfLossReporting,_P:dcfPtpPmHistStatsEnable,'dcfPtpProvisionedRemoteTP':dcfPtpProvisionedRemoteTP,'dcfPtpConformance':dcfPtpConformance,'dcfPtpCompliances':dcfPtpCompliances,'dcfPtpCompliance':dcfPtpCompliance,'dcfPtpGroups':dcfPtpGroups,_Q:dcfPtpGroup})