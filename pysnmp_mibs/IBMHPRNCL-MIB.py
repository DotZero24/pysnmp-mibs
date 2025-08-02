_E='ibmHprNclEnvId'
_D='IBMHPRNCL-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmArchitecture_ObjectIdentity=ObjectIdentity
ibmArchitecture=_IbmArchitecture_ObjectIdentity((1,3,6,1,4,1,2,5))
_Hpr_ObjectIdentity=ObjectIdentity
hpr=_Hpr_ObjectIdentity((1,3,6,1,4,1,2,5,10))
_IbmHprNcl_ObjectIdentity=ObjectIdentity
ibmHprNcl=_IbmHprNcl_ObjectIdentity((1,3,6,1,4,1,2,5,10,3))
_IbmHprNclGlobe_ObjectIdentity=ObjectIdentity
ibmHprNclGlobe=_IbmHprNclGlobe_ObjectIdentity((1,3,6,1,4,1,2,5,10,3,1))
class _IbmHprNclGlobeCtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notActive',1),('active',2)))
_IbmHprNclGlobeCtrState_Type.__name__=_C
_IbmHprNclGlobeCtrState_Object=MibScalar
ibmHprNclGlobeCtrState=_IbmHprNclGlobeCtrState_Object((1,3,6,1,4,1,2,5,10,3,1,1),_IbmHprNclGlobeCtrState_Type())
ibmHprNclGlobeCtrState.setMaxAccess('read-write')
if mibBuilder.loadTexts:ibmHprNclGlobeCtrState.setStatus(_A)
_IbmHprNclGlobeCtrStateTime_Type=TimeTicks
_IbmHprNclGlobeCtrStateTime_Object=MibScalar
ibmHprNclGlobeCtrStateTime=_IbmHprNclGlobeCtrStateTime_Object((1,3,6,1,4,1,2,5,10,3,1,2),_IbmHprNclGlobeCtrStateTime_Type())
ibmHprNclGlobeCtrStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclGlobeCtrStateTime.setStatus(_A)
_IbmHprNclGlobeAssignAnrs_Type=Counter32
_IbmHprNclGlobeAssignAnrs_Object=MibScalar
ibmHprNclGlobeAssignAnrs=_IbmHprNclGlobeAssignAnrs_Object((1,3,6,1,4,1,2,5,10,3,1,3),_IbmHprNclGlobeAssignAnrs_Type())
ibmHprNclGlobeAssignAnrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclGlobeAssignAnrs.setStatus(_A)
_IbmHprNclTable_Object=MibTable
ibmHprNclTable=_IbmHprNclTable_Object((1,3,6,1,4,1,2,5,10,3,2))
if mibBuilder.loadTexts:ibmHprNclTable.setStatus(_A)
_IbmHprNclEntry_Object=MibTableRow
ibmHprNclEntry=_IbmHprNclEntry_Object((1,3,6,1,4,1,2,5,10,3,2,1))
ibmHprNclEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibmHprNclEntry.setStatus(_A)
_IbmHprNclEnvId_Type=Gauge32
_IbmHprNclEnvId_Object=MibTableColumn
ibmHprNclEnvId=_IbmHprNclEnvId_Object((1,3,6,1,4,1,2,5,10,3,2,1,1),_IbmHprNclEnvId_Type())
ibmHprNclEnvId.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclEnvId.setStatus(_A)
_IbmHprNclDlcRecvNetFrames_Type=Counter32
_IbmHprNclDlcRecvNetFrames_Object=MibTableColumn
ibmHprNclDlcRecvNetFrames=_IbmHprNclDlcRecvNetFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,2),_IbmHprNclDlcRecvNetFrames_Type())
ibmHprNclDlcRecvNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvNetFrames.setStatus(_A)
_IbmHprNclDlcRecvHiFrames_Type=Counter32
_IbmHprNclDlcRecvHiFrames_Object=MibTableColumn
ibmHprNclDlcRecvHiFrames=_IbmHprNclDlcRecvHiFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,3),_IbmHprNclDlcRecvHiFrames_Type())
ibmHprNclDlcRecvHiFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvHiFrames.setStatus(_A)
_IbmHprNclDlcRecvMedFrames_Type=Counter32
_IbmHprNclDlcRecvMedFrames_Object=MibTableColumn
ibmHprNclDlcRecvMedFrames=_IbmHprNclDlcRecvMedFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,4),_IbmHprNclDlcRecvMedFrames_Type())
ibmHprNclDlcRecvMedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvMedFrames.setStatus(_A)
_IbmHprNclDlcRecvLoFrames_Type=Counter32
_IbmHprNclDlcRecvLoFrames_Object=MibTableColumn
ibmHprNclDlcRecvLoFrames=_IbmHprNclDlcRecvLoFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,5),_IbmHprNclDlcRecvLoFrames_Type())
ibmHprNclDlcRecvLoFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvLoFrames.setStatus(_A)
_IbmHprNclDlcRecvNetBytes_Type=Counter32
_IbmHprNclDlcRecvNetBytes_Object=MibTableColumn
ibmHprNclDlcRecvNetBytes=_IbmHprNclDlcRecvNetBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,6),_IbmHprNclDlcRecvNetBytes_Type())
ibmHprNclDlcRecvNetBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvNetBytes.setStatus(_A)
_IbmHprNclDlcRecvHiBytes_Type=Counter32
_IbmHprNclDlcRecvHiBytes_Object=MibTableColumn
ibmHprNclDlcRecvHiBytes=_IbmHprNclDlcRecvHiBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,7),_IbmHprNclDlcRecvHiBytes_Type())
ibmHprNclDlcRecvHiBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvHiBytes.setStatus(_A)
_IbmHprNclDlcRecvMedBytes_Type=Counter32
_IbmHprNclDlcRecvMedBytes_Object=MibTableColumn
ibmHprNclDlcRecvMedBytes=_IbmHprNclDlcRecvMedBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,8),_IbmHprNclDlcRecvMedBytes_Type())
ibmHprNclDlcRecvMedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvMedBytes.setStatus(_A)
_IbmHprNclDlcRecvLoBytes_Type=Counter32
_IbmHprNclDlcRecvLoBytes_Object=MibTableColumn
ibmHprNclDlcRecvLoBytes=_IbmHprNclDlcRecvLoBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,9),_IbmHprNclDlcRecvLoBytes_Type())
ibmHprNclDlcRecvLoBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvLoBytes.setStatus(_A)
_IbmHprNclDlcRecvAnrErrors_Type=Counter32
_IbmHprNclDlcRecvAnrErrors_Object=MibTableColumn
ibmHprNclDlcRecvAnrErrors=_IbmHprNclDlcRecvAnrErrors_Object((1,3,6,1,4,1,2,5,10,3,2,1,10),_IbmHprNclDlcRecvAnrErrors_Type())
ibmHprNclDlcRecvAnrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcRecvAnrErrors.setStatus(_A)
_IbmHprNclDlcSendNetFrames_Type=Counter32
_IbmHprNclDlcSendNetFrames_Object=MibTableColumn
ibmHprNclDlcSendNetFrames=_IbmHprNclDlcSendNetFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,11),_IbmHprNclDlcSendNetFrames_Type())
ibmHprNclDlcSendNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendNetFrames.setStatus(_A)
_IbmHprNclDlcSendHiFrames_Type=Counter32
_IbmHprNclDlcSendHiFrames_Object=MibTableColumn
ibmHprNclDlcSendHiFrames=_IbmHprNclDlcSendHiFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,12),_IbmHprNclDlcSendHiFrames_Type())
ibmHprNclDlcSendHiFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendHiFrames.setStatus(_A)
_IbmHprNclDlcSendMedFrames_Type=Counter32
_IbmHprNclDlcSendMedFrames_Object=MibTableColumn
ibmHprNclDlcSendMedFrames=_IbmHprNclDlcSendMedFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,13),_IbmHprNclDlcSendMedFrames_Type())
ibmHprNclDlcSendMedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendMedFrames.setStatus(_A)
_IbmHprNclDlcSendLoFrames_Type=Counter32
_IbmHprNclDlcSendLoFrames_Object=MibTableColumn
ibmHprNclDlcSendLoFrames=_IbmHprNclDlcSendLoFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,14),_IbmHprNclDlcSendLoFrames_Type())
ibmHprNclDlcSendLoFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendLoFrames.setStatus(_A)
_IbmHprNclDlcSendNetBytes_Type=Counter32
_IbmHprNclDlcSendNetBytes_Object=MibTableColumn
ibmHprNclDlcSendNetBytes=_IbmHprNclDlcSendNetBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,15),_IbmHprNclDlcSendNetBytes_Type())
ibmHprNclDlcSendNetBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendNetBytes.setStatus(_A)
_IbmHprNclDlcSendHiBytes_Type=Counter32
_IbmHprNclDlcSendHiBytes_Object=MibTableColumn
ibmHprNclDlcSendHiBytes=_IbmHprNclDlcSendHiBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,16),_IbmHprNclDlcSendHiBytes_Type())
ibmHprNclDlcSendHiBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendHiBytes.setStatus(_A)
_IbmHprNclDlcSendMedBytes_Type=Counter32
_IbmHprNclDlcSendMedBytes_Object=MibTableColumn
ibmHprNclDlcSendMedBytes=_IbmHprNclDlcSendMedBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,17),_IbmHprNclDlcSendMedBytes_Type())
ibmHprNclDlcSendMedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendMedBytes.setStatus(_A)
_IbmHprNclDlcSendLoBytes_Type=Counter32
_IbmHprNclDlcSendLoBytes_Object=MibTableColumn
ibmHprNclDlcSendLoBytes=_IbmHprNclDlcSendLoBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,18),_IbmHprNclDlcSendLoBytes_Type())
ibmHprNclDlcSendLoBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclDlcSendLoBytes.setStatus(_A)
_IbmHprNclRtpRecvNetFrames_Type=Counter32
_IbmHprNclRtpRecvNetFrames_Object=MibTableColumn
ibmHprNclRtpRecvNetFrames=_IbmHprNclRtpRecvNetFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,19),_IbmHprNclRtpRecvNetFrames_Type())
ibmHprNclRtpRecvNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvNetFrames.setStatus(_A)
_IbmHprNclRtpRecvHiFrames_Type=Counter32
_IbmHprNclRtpRecvHiFrames_Object=MibTableColumn
ibmHprNclRtpRecvHiFrames=_IbmHprNclRtpRecvHiFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,20),_IbmHprNclRtpRecvHiFrames_Type())
ibmHprNclRtpRecvHiFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvHiFrames.setStatus(_A)
_IbmHprNclRtpRecvMedFrames_Type=Counter32
_IbmHprNclRtpRecvMedFrames_Object=MibTableColumn
ibmHprNclRtpRecvMedFrames=_IbmHprNclRtpRecvMedFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,21),_IbmHprNclRtpRecvMedFrames_Type())
ibmHprNclRtpRecvMedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvMedFrames.setStatus(_A)
_IbmHprNclRtpRecvLoFrames_Type=Counter32
_IbmHprNclRtpRecvLoFrames_Object=MibTableColumn
ibmHprNclRtpRecvLoFrames=_IbmHprNclRtpRecvLoFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,22),_IbmHprNclRtpRecvLoFrames_Type())
ibmHprNclRtpRecvLoFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvLoFrames.setStatus(_A)
_IbmHprNclRtpRecvNetBytes_Type=Counter32
_IbmHprNclRtpRecvNetBytes_Object=MibTableColumn
ibmHprNclRtpRecvNetBytes=_IbmHprNclRtpRecvNetBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,23),_IbmHprNclRtpRecvNetBytes_Type())
ibmHprNclRtpRecvNetBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvNetBytes.setStatus(_A)
_IbmHprNclRtpRecvHiBytes_Type=Counter32
_IbmHprNclRtpRecvHiBytes_Object=MibTableColumn
ibmHprNclRtpRecvHiBytes=_IbmHprNclRtpRecvHiBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,24),_IbmHprNclRtpRecvHiBytes_Type())
ibmHprNclRtpRecvHiBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvHiBytes.setStatus(_A)
_IbmHprNclRtpRecvMedBytes_Type=Counter32
_IbmHprNclRtpRecvMedBytes_Object=MibTableColumn
ibmHprNclRtpRecvMedBytes=_IbmHprNclRtpRecvMedBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,25),_IbmHprNclRtpRecvMedBytes_Type())
ibmHprNclRtpRecvMedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvMedBytes.setStatus(_A)
_IbmHprNclRtpRecvLoBytes_Type=Counter32
_IbmHprNclRtpRecvLoBytes_Object=MibTableColumn
ibmHprNclRtpRecvLoBytes=_IbmHprNclRtpRecvLoBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,26),_IbmHprNclRtpRecvLoBytes_Type())
ibmHprNclRtpRecvLoBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvLoBytes.setStatus(_A)
_IbmHprNclRtpRecvAnrErrors_Type=Counter32
_IbmHprNclRtpRecvAnrErrors_Object=MibTableColumn
ibmHprNclRtpRecvAnrErrors=_IbmHprNclRtpRecvAnrErrors_Object((1,3,6,1,4,1,2,5,10,3,2,1,27),_IbmHprNclRtpRecvAnrErrors_Type())
ibmHprNclRtpRecvAnrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpRecvAnrErrors.setStatus(_A)
_IbmHprNclRtpSendNetFrames_Type=Counter32
_IbmHprNclRtpSendNetFrames_Object=MibTableColumn
ibmHprNclRtpSendNetFrames=_IbmHprNclRtpSendNetFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,28),_IbmHprNclRtpSendNetFrames_Type())
ibmHprNclRtpSendNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendNetFrames.setStatus(_A)
_IbmHprNclRtpSendHiFrames_Type=Counter32
_IbmHprNclRtpSendHiFrames_Object=MibTableColumn
ibmHprNclRtpSendHiFrames=_IbmHprNclRtpSendHiFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,29),_IbmHprNclRtpSendHiFrames_Type())
ibmHprNclRtpSendHiFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendHiFrames.setStatus(_A)
_IbmHprNclRtpSendMedFrames_Type=Counter32
_IbmHprNclRtpSendMedFrames_Object=MibTableColumn
ibmHprNclRtpSendMedFrames=_IbmHprNclRtpSendMedFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,30),_IbmHprNclRtpSendMedFrames_Type())
ibmHprNclRtpSendMedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendMedFrames.setStatus(_A)
_IbmHprNclRtpSendLoFrames_Type=Counter32
_IbmHprNclRtpSendLoFrames_Object=MibTableColumn
ibmHprNclRtpSendLoFrames=_IbmHprNclRtpSendLoFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,31),_IbmHprNclRtpSendLoFrames_Type())
ibmHprNclRtpSendLoFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendLoFrames.setStatus(_A)
_IbmHprNclRtpSendNetBytes_Type=Counter32
_IbmHprNclRtpSendNetBytes_Object=MibTableColumn
ibmHprNclRtpSendNetBytes=_IbmHprNclRtpSendNetBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,32),_IbmHprNclRtpSendNetBytes_Type())
ibmHprNclRtpSendNetBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendNetBytes.setStatus(_A)
_IbmHprNclRtpSendHiBytes_Type=Counter32
_IbmHprNclRtpSendHiBytes_Object=MibTableColumn
ibmHprNclRtpSendHiBytes=_IbmHprNclRtpSendHiBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,33),_IbmHprNclRtpSendHiBytes_Type())
ibmHprNclRtpSendHiBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendHiBytes.setStatus(_A)
_IbmHprNclRtpSendMedBytes_Type=Counter32
_IbmHprNclRtpSendMedBytes_Object=MibTableColumn
ibmHprNclRtpSendMedBytes=_IbmHprNclRtpSendMedBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,34),_IbmHprNclRtpSendMedBytes_Type())
ibmHprNclRtpSendMedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendMedBytes.setStatus(_A)
_IbmHprNclRtpSendLoBytes_Type=Counter32
_IbmHprNclRtpSendLoBytes_Object=MibTableColumn
ibmHprNclRtpSendLoBytes=_IbmHprNclRtpSendLoBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,35),_IbmHprNclRtpSendLoBytes_Type())
ibmHprNclRtpSendLoBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclRtpSendLoBytes.setStatus(_A)
_IbmHprNclInterSendNetFrames_Type=Counter32
_IbmHprNclInterSendNetFrames_Object=MibTableColumn
ibmHprNclInterSendNetFrames=_IbmHprNclInterSendNetFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,36),_IbmHprNclInterSendNetFrames_Type())
ibmHprNclInterSendNetFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendNetFrames.setStatus(_A)
_IbmHprNclInterSendHiFrames_Type=Counter32
_IbmHprNclInterSendHiFrames_Object=MibTableColumn
ibmHprNclInterSendHiFrames=_IbmHprNclInterSendHiFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,37),_IbmHprNclInterSendHiFrames_Type())
ibmHprNclInterSendHiFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendHiFrames.setStatus(_A)
_IbmHprNclInterSendMedFrames_Type=Counter32
_IbmHprNclInterSendMedFrames_Object=MibTableColumn
ibmHprNclInterSendMedFrames=_IbmHprNclInterSendMedFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,38),_IbmHprNclInterSendMedFrames_Type())
ibmHprNclInterSendMedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendMedFrames.setStatus(_A)
_IbmHprNclInterSendLoFrames_Type=Counter32
_IbmHprNclInterSendLoFrames_Object=MibTableColumn
ibmHprNclInterSendLoFrames=_IbmHprNclInterSendLoFrames_Object((1,3,6,1,4,1,2,5,10,3,2,1,39),_IbmHprNclInterSendLoFrames_Type())
ibmHprNclInterSendLoFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendLoFrames.setStatus(_A)
_IbmHprNclInterSendNetBytes_Type=Counter32
_IbmHprNclInterSendNetBytes_Object=MibTableColumn
ibmHprNclInterSendNetBytes=_IbmHprNclInterSendNetBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,40),_IbmHprNclInterSendNetBytes_Type())
ibmHprNclInterSendNetBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendNetBytes.setStatus(_A)
_IbmHprNclInterSendHiBytes_Type=Counter32
_IbmHprNclInterSendHiBytes_Object=MibTableColumn
ibmHprNclInterSendHiBytes=_IbmHprNclInterSendHiBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,41),_IbmHprNclInterSendHiBytes_Type())
ibmHprNclInterSendHiBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendHiBytes.setStatus(_A)
_IbmHprNclInterSendMedBytes_Type=Counter32
_IbmHprNclInterSendMedBytes_Object=MibTableColumn
ibmHprNclInterSendMedBytes=_IbmHprNclInterSendMedBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,42),_IbmHprNclInterSendMedBytes_Type())
ibmHprNclInterSendMedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendMedBytes.setStatus(_A)
_IbmHprNclInterSendLoBytes_Type=Counter32
_IbmHprNclInterSendLoBytes_Object=MibTableColumn
ibmHprNclInterSendLoBytes=_IbmHprNclInterSendLoBytes_Object((1,3,6,1,4,1,2,5,10,3,2,1,43),_IbmHprNclInterSendLoBytes_Type())
ibmHprNclInterSendLoBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprNclInterSendLoBytes.setStatus(_A)
_IbmHprNclCompliances_ObjectIdentity=ObjectIdentity
ibmHprNclCompliances=_IbmHprNclCompliances_ObjectIdentity((1,3,6,1,4,1,2,5,10,3,3))
_IbmHprNclConfGroups_ObjectIdentity=ObjectIdentity
ibmHprNclConfGroups=_IbmHprNclConfGroups_ObjectIdentity((1,3,6,1,4,1,2,5,10,3,4))
mibBuilder.exportSymbols(_D,**{'ibm':ibm,'ibmArchitecture':ibmArchitecture,'hpr':hpr,'ibmHprNcl':ibmHprNcl,'ibmHprNclGlobe':ibmHprNclGlobe,'ibmHprNclGlobeCtrState':ibmHprNclGlobeCtrState,'ibmHprNclGlobeCtrStateTime':ibmHprNclGlobeCtrStateTime,'ibmHprNclGlobeAssignAnrs':ibmHprNclGlobeAssignAnrs,'ibmHprNclTable':ibmHprNclTable,'ibmHprNclEntry':ibmHprNclEntry,_E:ibmHprNclEnvId,'ibmHprNclDlcRecvNetFrames':ibmHprNclDlcRecvNetFrames,'ibmHprNclDlcRecvHiFrames':ibmHprNclDlcRecvHiFrames,'ibmHprNclDlcRecvMedFrames':ibmHprNclDlcRecvMedFrames,'ibmHprNclDlcRecvLoFrames':ibmHprNclDlcRecvLoFrames,'ibmHprNclDlcRecvNetBytes':ibmHprNclDlcRecvNetBytes,'ibmHprNclDlcRecvHiBytes':ibmHprNclDlcRecvHiBytes,'ibmHprNclDlcRecvMedBytes':ibmHprNclDlcRecvMedBytes,'ibmHprNclDlcRecvLoBytes':ibmHprNclDlcRecvLoBytes,'ibmHprNclDlcRecvAnrErrors':ibmHprNclDlcRecvAnrErrors,'ibmHprNclDlcSendNetFrames':ibmHprNclDlcSendNetFrames,'ibmHprNclDlcSendHiFrames':ibmHprNclDlcSendHiFrames,'ibmHprNclDlcSendMedFrames':ibmHprNclDlcSendMedFrames,'ibmHprNclDlcSendLoFrames':ibmHprNclDlcSendLoFrames,'ibmHprNclDlcSendNetBytes':ibmHprNclDlcSendNetBytes,'ibmHprNclDlcSendHiBytes':ibmHprNclDlcSendHiBytes,'ibmHprNclDlcSendMedBytes':ibmHprNclDlcSendMedBytes,'ibmHprNclDlcSendLoBytes':ibmHprNclDlcSendLoBytes,'ibmHprNclRtpRecvNetFrames':ibmHprNclRtpRecvNetFrames,'ibmHprNclRtpRecvHiFrames':ibmHprNclRtpRecvHiFrames,'ibmHprNclRtpRecvMedFrames':ibmHprNclRtpRecvMedFrames,'ibmHprNclRtpRecvLoFrames':ibmHprNclRtpRecvLoFrames,'ibmHprNclRtpRecvNetBytes':ibmHprNclRtpRecvNetBytes,'ibmHprNclRtpRecvHiBytes':ibmHprNclRtpRecvHiBytes,'ibmHprNclRtpRecvMedBytes':ibmHprNclRtpRecvMedBytes,'ibmHprNclRtpRecvLoBytes':ibmHprNclRtpRecvLoBytes,'ibmHprNclRtpRecvAnrErrors':ibmHprNclRtpRecvAnrErrors,'ibmHprNclRtpSendNetFrames':ibmHprNclRtpSendNetFrames,'ibmHprNclRtpSendHiFrames':ibmHprNclRtpSendHiFrames,'ibmHprNclRtpSendMedFrames':ibmHprNclRtpSendMedFrames,'ibmHprNclRtpSendLoFrames':ibmHprNclRtpSendLoFrames,'ibmHprNclRtpSendNetBytes':ibmHprNclRtpSendNetBytes,'ibmHprNclRtpSendHiBytes':ibmHprNclRtpSendHiBytes,'ibmHprNclRtpSendMedBytes':ibmHprNclRtpSendMedBytes,'ibmHprNclRtpSendLoBytes':ibmHprNclRtpSendLoBytes,'ibmHprNclInterSendNetFrames':ibmHprNclInterSendNetFrames,'ibmHprNclInterSendHiFrames':ibmHprNclInterSendHiFrames,'ibmHprNclInterSendMedFrames':ibmHprNclInterSendMedFrames,'ibmHprNclInterSendLoFrames':ibmHprNclInterSendLoFrames,'ibmHprNclInterSendNetBytes':ibmHprNclInterSendNetBytes,'ibmHprNclInterSendHiBytes':ibmHprNclInterSendHiBytes,'ibmHprNclInterSendMedBytes':ibmHprNclInterSendMedBytes,'ibmHprNclInterSendLoBytes':ibmHprNclInterSendLoBytes,'ibmHprNclCompliances':ibmHprNclCompliances,'ibmHprNclConfGroups':ibmHprNclConfGroups})