_Q='configGroup20'
_P='configGroup10'
_O='cfgActiveImageBootLocation'
_N='cfgActiveImageVersion'
_M='cfgLastErrorReason'
_L='cfgLastError'
_K='cfgActivateFile'
_J='cfgTransferStatus'
_I='cfgActivateTransfer'
_H='cfgFileName'
_G='cfgManagerAddress'
_F='cfgTransferOp'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='current'
_A='CTRON-SSR-CONFIG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ssrMibs,=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ssrConfigMIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,230))
if mibBuilder.loadTexts:ssrConfigMIB.setRevisions(('2000-07-15 00:00','2000-02-20 00:00','1998-08-17 00:00'))
class SSRErrorCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noStatus',1),('timeout',2),('networkError',3),('noSpace',4),('invalidConfig',5),('commandCompleted',6),('internalError',7),('tftpServerError',8)))
_ConfigConformance_ObjectIdentity=ObjectIdentity
configConformance=_ConfigConformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,230,3))
_ConfigCompliances_ObjectIdentity=ObjectIdentity
configCompliances=_ConfigCompliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,230,3,1))
_ConfigGroups_ObjectIdentity=ObjectIdentity
configGroups=_ConfigGroups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,230,3,2))
_CfgGroup_ObjectIdentity=ObjectIdentity
cfgGroup=_CfgGroup_ObjectIdentity((1,3,6,1,4,1,52,2501,1,231))
class _CfgTransferOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noop',1),('sendConfigToAgent',2),('receiveConfigFromAgent',3),('receiveBootlogFromAgent',4)))
_CfgTransferOp_Type.__name__=_E
_CfgTransferOp_Object=MibScalar
cfgTransferOp=_CfgTransferOp_Object((1,3,6,1,4,1,52,2501,1,231,1),_CfgTransferOp_Type())
cfgTransferOp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgTransferOp.setStatus(_B)
_CfgManagerAddress_Type=IpAddress
_CfgManagerAddress_Object=MibScalar
cfgManagerAddress=_CfgManagerAddress_Object((1,3,6,1,4,1,52,2501,1,231,2),_CfgManagerAddress_Type())
cfgManagerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgManagerAddress.setStatus(_B)
_CfgFileName_Type=DisplayString
_CfgFileName_Object=MibScalar
cfgFileName=_CfgFileName_Object((1,3,6,1,4,1,52,2501,1,231,3),_CfgFileName_Type())
cfgFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgFileName.setStatus(_B)
_CfgActivateTransfer_Type=TruthValue
_CfgActivateTransfer_Object=MibScalar
cfgActivateTransfer=_CfgActivateTransfer_Object((1,3,6,1,4,1,52,2501,1,231,4),_CfgActivateTransfer_Type())
cfgActivateTransfer.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgActivateTransfer.setStatus(_B)
class _CfgTransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('sending',2),('receiving',3),('transferComplete',4),('error',5)))
_CfgTransferStatus_Type.__name__=_E
_CfgTransferStatus_Object=MibScalar
cfgTransferStatus=_CfgTransferStatus_Object((1,3,6,1,4,1,52,2501,1,231,5),_CfgTransferStatus_Type())
cfgTransferStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgTransferStatus.setStatus(_B)
_CfgActivateFile_Type=TruthValue
_CfgActivateFile_Object=MibScalar
cfgActivateFile=_CfgActivateFile_Object((1,3,6,1,4,1,52,2501,1,231,6),_CfgActivateFile_Type())
cfgActivateFile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgActivateFile.setStatus(_B)
_CfgLastError_Type=SSRErrorCode
_CfgLastError_Object=MibScalar
cfgLastError=_CfgLastError_Object((1,3,6,1,4,1,52,2501,1,231,7),_CfgLastError_Type())
cfgLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgLastError.setStatus(_B)
_CfgLastErrorReason_Type=DisplayString
_CfgLastErrorReason_Object=MibScalar
cfgLastErrorReason=_CfgLastErrorReason_Object((1,3,6,1,4,1,52,2501,1,231,8),_CfgLastErrorReason_Type())
cfgLastErrorReason.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgLastErrorReason.setStatus(_B)
_CfgActiveImageVersion_Type=DisplayString
_CfgActiveImageVersion_Object=MibScalar
cfgActiveImageVersion=_CfgActiveImageVersion_Object((1,3,6,1,4,1,52,2501,1,231,9),_CfgActiveImageVersion_Type())
cfgActiveImageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgActiveImageVersion.setStatus(_B)
_CfgActiveImageBootLocation_Type=DisplayString
_CfgActiveImageBootLocation_Object=MibScalar
cfgActiveImageBootLocation=_CfgActiveImageBootLocation_Object((1,3,6,1,4,1,52,2501,1,231,10),_CfgActiveImageBootLocation_Type())
cfgActiveImageBootLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgActiveImageBootLocation.setStatus(_B)
configGroup10=ObjectGroup((1,3,6,1,4,1,52,2501,1,230,3,2,1))
configGroup10.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:configGroup10.setStatus('deprecated')
configGroup20=ObjectGroup((1,3,6,1,4,1,52,2501,1,230,3,2,2))
configGroup20.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:configGroup20.setStatus(_B)
configCompliance=ModuleCompliance((1,3,6,1,4,1,52,2501,1,230,3,1,1))
configCompliance.setObjects((_A,_P))
if mibBuilder.loadTexts:configCompliance.setStatus('obsolete')
configCompliance2=ModuleCompliance((1,3,6,1,4,1,52,2501,1,230,3,1,2))
configCompliance2.setObjects((_A,_Q))
if mibBuilder.loadTexts:configCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SSRErrorCode':SSRErrorCode,'ssrConfigMIB':ssrConfigMIB,'configConformance':configConformance,'configCompliances':configCompliances,'configCompliance':configCompliance,'configCompliance2':configCompliance2,'configGroups':configGroups,_P:configGroup10,_Q:configGroup20,'cfgGroup':cfgGroup,_F:cfgTransferOp,_G:cfgManagerAddress,_H:cfgFileName,_I:cfgActivateTransfer,_J:cfgTransferStatus,_K:cfgActivateFile,_L:cfgLastError,_M:cfgLastErrorReason,_N:cfgActiveImageVersion,_O:cfgActiveImageBootLocation})