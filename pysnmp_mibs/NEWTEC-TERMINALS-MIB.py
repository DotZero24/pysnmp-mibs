_R='ntcTermsConfGrpV1Standard'
_Q='ntcTermsAdminState'
_P='ntcTermsCtrlIpAddr'
_O='ntcTermsId'
_N='ntcTermsCfgStateRowStatus'
_M='ntcTermsMonEsNo'
_L='ntcTermsMonState'
_K='ntcTermsMonName'
_J='ntcTermsCfgStateName'
_I='not-accessible'
_H='ntcTermsMonStateInx'
_G='Unsigned32'
_F='read-only'
_E='DisplayString'
_D='Integer32'
_C='read-create'
_B='NEWTEC-TERMINALS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
ntcTerminals=ModuleIdentity((1,3,6,1,4,1,5835,5,2,2700))
if mibBuilder.loadTexts:ntcTerminals.setRevisions(('2018-02-02 09:00','2015-04-13 07:00','2014-07-15 08:00','2014-02-03 12:00','2013-01-08 12:00'))
_NtcTermsObjects_ObjectIdentity=ObjectIdentity
ntcTermsObjects=_NtcTermsObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2700,1))
if mibBuilder.loadTexts:ntcTermsObjects.setStatus(_A)
_NtcTermsMon_ObjectIdentity=ObjectIdentity
ntcTermsMon=_NtcTermsMon_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2700,1,1))
if mibBuilder.loadTexts:ntcTermsMon.setStatus(_A)
_NtcTermsMonStateTable_Object=MibTable
ntcTermsMonStateTable=_NtcTermsMonStateTable_Object((1,3,6,1,4,1,5835,5,2,2700,1,1,1))
if mibBuilder.loadTexts:ntcTermsMonStateTable.setStatus(_A)
_NtcTermsMonStateEntry_Object=MibTableRow
ntcTermsMonStateEntry=_NtcTermsMonStateEntry_Object((1,3,6,1,4,1,5835,5,2,2700,1,1,1,1))
ntcTermsMonStateEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ntcTermsMonStateEntry.setStatus(_A)
_NtcTermsMonStateInx_Type=Unsigned32
_NtcTermsMonStateInx_Object=MibTableColumn
ntcTermsMonStateInx=_NtcTermsMonStateInx_Object((1,3,6,1,4,1,5835,5,2,2700,1,1,1,1,1),_NtcTermsMonStateInx_Type())
ntcTermsMonStateInx.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTermsMonStateInx.setStatus(_A)
class _NtcTermsMonName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcTermsMonName_Type.__name__=_E
_NtcTermsMonName_Object=MibTableColumn
ntcTermsMonName=_NtcTermsMonName_Object((1,3,6,1,4,1,5835,5,2,2700,1,1,1,1,2),_NtcTermsMonName_Type())
ntcTermsMonName.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTermsMonName.setStatus(_A)
class _NtcTermsMonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcTermsMonState_Type.__name__=_D
_NtcTermsMonState_Object=MibTableColumn
ntcTermsMonState=_NtcTermsMonState_Object((1,3,6,1,4,1,5835,5,2,2700,1,1,1,1,3),_NtcTermsMonState_Type())
ntcTermsMonState.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTermsMonState.setStatus(_A)
class _NtcTermsMonEsNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,3000))
_NtcTermsMonEsNo_Type.__name__=_D
_NtcTermsMonEsNo_Object=MibTableColumn
ntcTermsMonEsNo=_NtcTermsMonEsNo_Object((1,3,6,1,4,1,5835,5,2,2700,1,1,1,1,4),_NtcTermsMonEsNo_Type())
ntcTermsMonEsNo.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcTermsMonEsNo.setStatus(_A)
if mibBuilder.loadTexts:ntcTermsMonEsNo.setUnits('dB')
_NtcTermsCfgStateTable_Object=MibTable
ntcTermsCfgStateTable=_NtcTermsCfgStateTable_Object((1,3,6,1,4,1,5835,5,2,2700,1,2))
if mibBuilder.loadTexts:ntcTermsCfgStateTable.setStatus(_A)
_NtcTermsCfgStateEntry_Object=MibTableRow
ntcTermsCfgStateEntry=_NtcTermsCfgStateEntry_Object((1,3,6,1,4,1,5835,5,2,2700,1,2,1))
ntcTermsCfgStateEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ntcTermsCfgStateEntry.setStatus(_A)
class _NtcTermsCfgStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_NtcTermsCfgStateName_Type.__name__=_E
_NtcTermsCfgStateName_Object=MibTableColumn
ntcTermsCfgStateName=_NtcTermsCfgStateName_Object((1,3,6,1,4,1,5835,5,2,2700,1,2,1,1),_NtcTermsCfgStateName_Type())
ntcTermsCfgStateName.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcTermsCfgStateName.setStatus(_A)
_NtcTermsCfgStateRowStatus_Type=RowStatus
_NtcTermsCfgStateRowStatus_Object=MibTableColumn
ntcTermsCfgStateRowStatus=_NtcTermsCfgStateRowStatus_Object((1,3,6,1,4,1,5835,5,2,2700,1,2,1,2),_NtcTermsCfgStateRowStatus_Type())
ntcTermsCfgStateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTermsCfgStateRowStatus.setStatus(_A)
class _NtcTermsId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65277))
_NtcTermsId_Type.__name__=_G
_NtcTermsId_Object=MibTableColumn
ntcTermsId=_NtcTermsId_Object((1,3,6,1,4,1,5835,5,2,2700,1,2,1,3),_NtcTermsId_Type())
ntcTermsId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTermsId.setStatus(_A)
_NtcTermsCtrlIpAddr_Type=IpAddress
_NtcTermsCtrlIpAddr_Object=MibTableColumn
ntcTermsCtrlIpAddr=_NtcTermsCtrlIpAddr_Object((1,3,6,1,4,1,5835,5,2,2700,1,2,1,4),_NtcTermsCtrlIpAddr_Type())
ntcTermsCtrlIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTermsCtrlIpAddr.setStatus(_A)
_NtcTermsAdminState_Type=NtcEnable
_NtcTermsAdminState_Object=MibTableColumn
ntcTermsAdminState=_NtcTermsAdminState_Object((1,3,6,1,4,1,5835,5,2,2700,1,2,1,5),_NtcTermsAdminState_Type())
ntcTermsAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTermsAdminState.setStatus(_A)
_NtcTermsConformance_ObjectIdentity=ObjectIdentity
ntcTermsConformance=_NtcTermsConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2700,2))
if mibBuilder.loadTexts:ntcTermsConformance.setStatus(_A)
_NtcTermsConfCompliance_ObjectIdentity=ObjectIdentity
ntcTermsConfCompliance=_NtcTermsConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2700,2,1))
if mibBuilder.loadTexts:ntcTermsConfCompliance.setStatus(_A)
_NtcTermsConfGroup_ObjectIdentity=ObjectIdentity
ntcTermsConfGroup=_NtcTermsConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2700,2,2))
if mibBuilder.loadTexts:ntcTermsConfGroup.setStatus(_A)
ntcTermsConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,2700,2,2,1))
ntcTermsConfGrpV1Standard.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ntcTermsConfGrpV1Standard.setStatus(_A)
ntcTermsConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,2700,2,1,1))
ntcTermsConfCompV1Standard.setObjects((_B,_R))
if mibBuilder.loadTexts:ntcTermsConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTerminals':ntcTerminals,'ntcTermsObjects':ntcTermsObjects,'ntcTermsMon':ntcTermsMon,'ntcTermsMonStateTable':ntcTermsMonStateTable,'ntcTermsMonStateEntry':ntcTermsMonStateEntry,_H:ntcTermsMonStateInx,_K:ntcTermsMonName,_L:ntcTermsMonState,_M:ntcTermsMonEsNo,'ntcTermsCfgStateTable':ntcTermsCfgStateTable,'ntcTermsCfgStateEntry':ntcTermsCfgStateEntry,_J:ntcTermsCfgStateName,_N:ntcTermsCfgStateRowStatus,_O:ntcTermsId,_P:ntcTermsCtrlIpAddr,_Q:ntcTermsAdminState,'ntcTermsConformance':ntcTermsConformance,'ntcTermsConfCompliance':ntcTermsConfCompliance,'ntcTermsConfCompV1Standard':ntcTermsConfCompV1Standard,'ntcTermsConfGroup':ntcTermsConfGroup,_R:ntcTermsConfGrpV1Standard})