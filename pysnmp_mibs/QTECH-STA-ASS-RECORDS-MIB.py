_AR='qtechStaAssStatisticsMIBroup'
_AQ='qtechStaAssRetrySearchByMACMIBroup'
_AP='qtechStaAssSignalSearchByMACMIBroup'
_AO='qtechStaAssRecordsSearchByAPMIBroup'
_AN='qtechStaAssRecordsSearchByTimeMIBroup'
_AM='qtechStaAssRecordsMIBroup'
_AL='qtechStaAssRecordsGrobalMIBroup'
_AK='qtechAssStatisticsObligate3'
_AJ='qtechAssStatisticsObligate2'
_AI='qtechAssStatisticsObligate1'
_AH='qtechAssStatisticsdown'
_AG='qtechAssStatisticsTotalinfo'
_AF='qtechAssStatisticsTotalsta'
_AE='qtechStaRetryValue'
_AD='qtechStaRetrytime'
_AC='qtechStaSignalValue'
_AB='qtechStaSignaltime'
_AA='qtechStaAPSSID'
_A9='qtechStaAPlatelytime'
_A8='qtechStaAPjointimes'
_A7='qtechStaAPjitter'
_A6='qtechStaAPtotaltimes'
_A5='qtechStaAProamtimes'
_A4='qtechStaAPupdowntimes'
_A3='qtechStaAPStartime'
_A2='qtechStaAPISUP'
_A1='qtechStaAPMac'
_A0='qtechStaTimerSSID'
_z='qtechStaTimerlatelytime'
_y='qtechStaTimerjointimes'
_x='qtechStaTimerjitter'
_w='qtechStaTimertotaltimes'
_v='qtechStaTimeroamtimes'
_u='qtechStaTimeupdowntimes'
_t='qtechStaTimeStartime'
_s='qtechStaTimeISUP'
_r='qtechStaTimeAPName'
_q='qtechStaTimeMac'
_p='qtechStaAssSSID'
_o='qtechStaAsslatelytime'
_n='qtechStaAssjointimes'
_m='qtechStaAssjitter'
_l='qtechStaAssRoamtype'
_k='qtechStaAssSignalQua'
_j='qtechStaAssApNameNow'
_i='qtechStaAssApNamePre'
_h='qtechStaAssReason'
_g='qtechStaAssResult'
_f='qtechStaAssSubAction'
_e='qtechStaAssAction'
_d='qtechStaAsstime'
_c='qtechStaMacGrobalSSID'
_b='qtechStaMacGrobalrealdowntimes'
_a='qtechStaMacGrobaltotaltimes'
_Z='qtechStaMacGrobalroamtimes'
_Y='qtechStaMacGrobalupdowntimes'
_X='qtechStaMacGrobalStartime'
_W='qtechStaMacGrobalISUP'
_V='qtechStaMacGrobalAPName'
_U='qtechStaRetryMacindex'
_T='qtechStaRetryMacAddress'
_S='qtechStaSignalMacindex'
_R='qtechStaSignalMacAddress'
_Q='qtechStaAPindex'
_P='qtechStaAPAPName'
_O='qtechStaTimeindex'
_N='qtechStaDowntimeHigh'
_M='qtechStaDowntimeLow'
_L='qtechStaUptimeHigh'
_K='qtechStaUptimeLow'
_J='qtechStaMacindex'
_I='qtechStaMacAddress'
_H='qtechStaMacGrobalAddress'
_G='down'
_F='Integer32'
_E='DisplayString'
_D='not-accessible'
_C='read-only'
_B='QTECH-STA-ASS-RECORDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechIfIndex,=mibBuilder.importSymbols('QTECH-INTERFACE-MIB','qtechIfIndex')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechStaAssRecordsMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,101))
if mibBuilder.loadTexts:qtechStaAssRecordsMIB.setRevisions(('2009-11-10 00:00',))
_QtechStaAssRecordsMIBTrap_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsMIBTrap=_QtechStaAssRecordsMIBTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,0))
_QtechStaAssRecordsMIBObjects_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsMIBObjects=_QtechStaAssRecordsMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1))
_QtechStaAssRecordsGrobal_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsGrobal=_QtechStaAssRecordsGrobal_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,1))
_QtechStaAssRecordsGrobalTable_Object=MibTable
qtechStaAssRecordsGrobalTable=_QtechStaAssRecordsGrobalTable_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1))
if mibBuilder.loadTexts:qtechStaAssRecordsGrobalTable.setStatus(_A)
_QtechStaAssRecordsGrobalEntry_Object=MibTableRow
qtechStaAssRecordsGrobalEntry=_QtechStaAssRecordsGrobalEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1))
qtechStaAssRecordsGrobalEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechStaAssRecordsGrobalEntry.setStatus(_A)
_QtechStaMacGrobalAddress_Type=MacAddress
_QtechStaMacGrobalAddress_Object=MibTableColumn
qtechStaMacGrobalAddress=_QtechStaMacGrobalAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,1),_QtechStaMacGrobalAddress_Type())
qtechStaMacGrobalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaMacGrobalAddress.setStatus(_A)
class _QtechStaMacGrobalAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechStaMacGrobalAPName_Type.__name__=_E
_QtechStaMacGrobalAPName_Object=MibTableColumn
qtechStaMacGrobalAPName=_QtechStaMacGrobalAPName_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,2),_QtechStaMacGrobalAPName_Type())
qtechStaMacGrobalAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalAPName.setStatus(_A)
class _QtechStaMacGrobalISUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_QtechStaMacGrobalISUP_Type.__name__=_F
_QtechStaMacGrobalISUP_Object=MibTableColumn
qtechStaMacGrobalISUP=_QtechStaMacGrobalISUP_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,3),_QtechStaMacGrobalISUP_Type())
qtechStaMacGrobalISUP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalISUP.setStatus(_A)
_QtechStaMacGrobalStartime_Type=DateAndTime
_QtechStaMacGrobalStartime_Object=MibTableColumn
qtechStaMacGrobalStartime=_QtechStaMacGrobalStartime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,4),_QtechStaMacGrobalStartime_Type())
qtechStaMacGrobalStartime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalStartime.setStatus(_A)
_QtechStaMacGrobalupdowntimes_Type=Unsigned32
_QtechStaMacGrobalupdowntimes_Object=MibTableColumn
qtechStaMacGrobalupdowntimes=_QtechStaMacGrobalupdowntimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,5),_QtechStaMacGrobalupdowntimes_Type())
qtechStaMacGrobalupdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalupdowntimes.setStatus(_A)
_QtechStaMacGrobalroamtimes_Type=Unsigned32
_QtechStaMacGrobalroamtimes_Object=MibTableColumn
qtechStaMacGrobalroamtimes=_QtechStaMacGrobalroamtimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,6),_QtechStaMacGrobalroamtimes_Type())
qtechStaMacGrobalroamtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalroamtimes.setStatus(_A)
_QtechStaMacGrobaltotaltimes_Type=Unsigned32
_QtechStaMacGrobaltotaltimes_Object=MibTableColumn
qtechStaMacGrobaltotaltimes=_QtechStaMacGrobaltotaltimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,7),_QtechStaMacGrobaltotaltimes_Type())
qtechStaMacGrobaltotaltimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobaltotaltimes.setStatus(_A)
_QtechStaMacGrobalrealdowntimes_Type=Unsigned32
_QtechStaMacGrobalrealdowntimes_Object=MibTableColumn
qtechStaMacGrobalrealdowntimes=_QtechStaMacGrobalrealdowntimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,8),_QtechStaMacGrobalrealdowntimes_Type())
qtechStaMacGrobalrealdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalrealdowntimes.setStatus(_A)
class _QtechStaMacGrobalSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechStaMacGrobalSSID_Type.__name__=_E
_QtechStaMacGrobalSSID_Object=MibTableColumn
qtechStaMacGrobalSSID=_QtechStaMacGrobalSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,1,1,1,9),_QtechStaMacGrobalSSID_Type())
qtechStaMacGrobalSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaMacGrobalSSID.setStatus(_A)
_QtechStaAssRecordsByMAC_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsByMAC=_QtechStaAssRecordsByMAC_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,2))
_QtechStaAssRecordsByMACTable_Object=MibTable
qtechStaAssRecordsByMACTable=_QtechStaAssRecordsByMACTable_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1))
if mibBuilder.loadTexts:qtechStaAssRecordsByMACTable.setStatus(_A)
_QtechStaAssRecordsByMACEntry_Object=MibTableRow
qtechStaAssRecordsByMACEntry=_QtechStaAssRecordsByMACEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1))
qtechStaAssRecordsByMACEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:qtechStaAssRecordsByMACEntry.setStatus(_A)
_QtechStaMacAddress_Type=MacAddress
_QtechStaMacAddress_Object=MibTableColumn
qtechStaMacAddress=_QtechStaMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,1),_QtechStaMacAddress_Type())
qtechStaMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaMacAddress.setStatus(_A)
_QtechStaMacindex_Type=Unsigned32
_QtechStaMacindex_Object=MibTableColumn
qtechStaMacindex=_QtechStaMacindex_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,2),_QtechStaMacindex_Type())
qtechStaMacindex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaMacindex.setStatus(_A)
_QtechStaAsstime_Type=DateAndTime
_QtechStaAsstime_Object=MibTableColumn
qtechStaAsstime=_QtechStaAsstime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,3),_QtechStaAsstime_Type())
qtechStaAsstime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAsstime.setStatus(_A)
class _QtechStaAssAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('join',1),('leave',2),('roam',3),('delete',4)))
_QtechStaAssAction_Type.__name__=_F
_QtechStaAssAction_Object=MibTableColumn
qtechStaAssAction=_QtechStaAssAction_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,4),_QtechStaAssAction_Type())
qtechStaAssAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssAction.setStatus(_A)
_QtechStaAssSubAction_Type=Integer32
_QtechStaAssSubAction_Object=MibTableColumn
qtechStaAssSubAction=_QtechStaAssSubAction_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,5),_QtechStaAssSubAction_Type())
qtechStaAssSubAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssSubAction.setStatus(_A)
class _QtechStaAssResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('success',0),('failed',1)))
_QtechStaAssResult_Type.__name__=_F
_QtechStaAssResult_Object=MibTableColumn
qtechStaAssResult=_QtechStaAssResult_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,6),_QtechStaAssResult_Type())
qtechStaAssResult.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssResult.setStatus(_A)
_QtechStaAssReason_Type=Integer32
_QtechStaAssReason_Object=MibTableColumn
qtechStaAssReason=_QtechStaAssReason_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,7),_QtechStaAssReason_Type())
qtechStaAssReason.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssReason.setStatus(_A)
class _QtechStaAssApNamePre_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechStaAssApNamePre_Type.__name__=_E
_QtechStaAssApNamePre_Object=MibTableColumn
qtechStaAssApNamePre=_QtechStaAssApNamePre_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,8),_QtechStaAssApNamePre_Type())
qtechStaAssApNamePre.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssApNamePre.setStatus(_A)
class _QtechStaAssApNameNow_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechStaAssApNameNow_Type.__name__=_E
_QtechStaAssApNameNow_Object=MibTableColumn
qtechStaAssApNameNow=_QtechStaAssApNameNow_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,9),_QtechStaAssApNameNow_Type())
qtechStaAssApNameNow.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssApNameNow.setStatus(_A)
_QtechStaAssSignalQua_Type=Integer32
_QtechStaAssSignalQua_Object=MibTableColumn
qtechStaAssSignalQua=_QtechStaAssSignalQua_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,10),_QtechStaAssSignalQua_Type())
qtechStaAssSignalQua.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssSignalQua.setStatus(_A)
_QtechStaAssRoamtype_Type=Integer32
_QtechStaAssRoamtype_Object=MibTableColumn
qtechStaAssRoamtype=_QtechStaAssRoamtype_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,11),_QtechStaAssRoamtype_Type())
qtechStaAssRoamtype.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssRoamtype.setStatus(_A)
_QtechStaAssjitter_Type=Integer32
_QtechStaAssjitter_Object=MibTableColumn
qtechStaAssjitter=_QtechStaAssjitter_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,12),_QtechStaAssjitter_Type())
qtechStaAssjitter.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssjitter.setStatus(_A)
_QtechStaAssjointimes_Type=Unsigned32
_QtechStaAssjointimes_Object=MibTableColumn
qtechStaAssjointimes=_QtechStaAssjointimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,13),_QtechStaAssjointimes_Type())
qtechStaAssjointimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssjointimes.setStatus(_A)
_QtechStaAsslatelytime_Type=DateAndTime
_QtechStaAsslatelytime_Object=MibTableColumn
qtechStaAsslatelytime=_QtechStaAsslatelytime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,14),_QtechStaAsslatelytime_Type())
qtechStaAsslatelytime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAsslatelytime.setStatus(_A)
_QtechStaAssSSID_Type=DisplayString
_QtechStaAssSSID_Object=MibTableColumn
qtechStaAssSSID=_QtechStaAssSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,2,1,1,15),_QtechStaAssSSID_Type())
qtechStaAssSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAssSSID.setStatus(_A)
_QtechStaAssRecordsByTime_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsByTime=_QtechStaAssRecordsByTime_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,3))
_QtechStaAssRecordsSearchByTimeTable_Object=MibTable
qtechStaAssRecordsSearchByTimeTable=_QtechStaAssRecordsSearchByTimeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1))
if mibBuilder.loadTexts:qtechStaAssRecordsSearchByTimeTable.setStatus(_A)
_QtechStaAssRecordsSearchByTimeEntry_Object=MibTableRow
qtechStaAssRecordsSearchByTimeEntry=_QtechStaAssRecordsSearchByTimeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1))
qtechStaAssRecordsSearchByTimeEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:qtechStaAssRecordsSearchByTimeEntry.setStatus(_A)
_QtechStaUptimeLow_Type=DateAndTime
_QtechStaUptimeLow_Object=MibTableColumn
qtechStaUptimeLow=_QtechStaUptimeLow_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,1),_QtechStaUptimeLow_Type())
qtechStaUptimeLow.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaUptimeLow.setStatus(_A)
_QtechStaUptimeHigh_Type=DateAndTime
_QtechStaUptimeHigh_Object=MibTableColumn
qtechStaUptimeHigh=_QtechStaUptimeHigh_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,2),_QtechStaUptimeHigh_Type())
qtechStaUptimeHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaUptimeHigh.setStatus(_A)
_QtechStaDowntimeLow_Type=DateAndTime
_QtechStaDowntimeLow_Object=MibTableColumn
qtechStaDowntimeLow=_QtechStaDowntimeLow_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,3),_QtechStaDowntimeLow_Type())
qtechStaDowntimeLow.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaDowntimeLow.setStatus(_A)
_QtechStaDowntimeHigh_Type=DateAndTime
_QtechStaDowntimeHigh_Object=MibTableColumn
qtechStaDowntimeHigh=_QtechStaDowntimeHigh_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,4),_QtechStaDowntimeHigh_Type())
qtechStaDowntimeHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaDowntimeHigh.setStatus(_A)
_QtechStaTimeindex_Type=Unsigned32
_QtechStaTimeindex_Object=MibTableColumn
qtechStaTimeindex=_QtechStaTimeindex_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,5),_QtechStaTimeindex_Type())
qtechStaTimeindex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaTimeindex.setStatus(_A)
_QtechStaTimeMac_Type=MacAddress
_QtechStaTimeMac_Object=MibTableColumn
qtechStaTimeMac=_QtechStaTimeMac_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,6),_QtechStaTimeMac_Type())
qtechStaTimeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimeMac.setStatus(_A)
class _QtechStaTimeAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechStaTimeAPName_Type.__name__=_E
_QtechStaTimeAPName_Object=MibTableColumn
qtechStaTimeAPName=_QtechStaTimeAPName_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,7),_QtechStaTimeAPName_Type())
qtechStaTimeAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimeAPName.setStatus(_A)
class _QtechStaTimeISUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_QtechStaTimeISUP_Type.__name__=_F
_QtechStaTimeISUP_Object=MibTableColumn
qtechStaTimeISUP=_QtechStaTimeISUP_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,8),_QtechStaTimeISUP_Type())
qtechStaTimeISUP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimeISUP.setStatus(_A)
_QtechStaTimeStartime_Type=DateAndTime
_QtechStaTimeStartime_Object=MibTableColumn
qtechStaTimeStartime=_QtechStaTimeStartime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,9),_QtechStaTimeStartime_Type())
qtechStaTimeStartime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimeStartime.setStatus(_A)
_QtechStaTimeupdowntimes_Type=Unsigned32
_QtechStaTimeupdowntimes_Object=MibTableColumn
qtechStaTimeupdowntimes=_QtechStaTimeupdowntimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,10),_QtechStaTimeupdowntimes_Type())
qtechStaTimeupdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimeupdowntimes.setStatus(_A)
_QtechStaTimeroamtimes_Type=Unsigned32
_QtechStaTimeroamtimes_Object=MibTableColumn
qtechStaTimeroamtimes=_QtechStaTimeroamtimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,11),_QtechStaTimeroamtimes_Type())
qtechStaTimeroamtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimeroamtimes.setStatus(_A)
_QtechStaTimertotaltimes_Type=Unsigned32
_QtechStaTimertotaltimes_Object=MibTableColumn
qtechStaTimertotaltimes=_QtechStaTimertotaltimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,12),_QtechStaTimertotaltimes_Type())
qtechStaTimertotaltimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimertotaltimes.setStatus(_A)
_QtechStaTimerjitter_Type=Integer32
_QtechStaTimerjitter_Object=MibTableColumn
qtechStaTimerjitter=_QtechStaTimerjitter_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,13),_QtechStaTimerjitter_Type())
qtechStaTimerjitter.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimerjitter.setStatus(_A)
_QtechStaTimerjointimes_Type=Unsigned32
_QtechStaTimerjointimes_Object=MibTableColumn
qtechStaTimerjointimes=_QtechStaTimerjointimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,14),_QtechStaTimerjointimes_Type())
qtechStaTimerjointimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimerjointimes.setStatus(_A)
_QtechStaTimerlatelytime_Type=DateAndTime
_QtechStaTimerlatelytime_Object=MibTableColumn
qtechStaTimerlatelytime=_QtechStaTimerlatelytime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,15),_QtechStaTimerlatelytime_Type())
qtechStaTimerlatelytime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimerlatelytime.setStatus(_A)
_QtechStaTimerSSID_Type=DisplayString
_QtechStaTimerSSID_Object=MibTableColumn
qtechStaTimerSSID=_QtechStaTimerSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,3,1,1,16),_QtechStaTimerSSID_Type())
qtechStaTimerSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaTimerSSID.setStatus(_A)
_QtechStaAssRecordsByAP_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsByAP=_QtechStaAssRecordsByAP_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,4))
_QtechStaAssRecordsSearchByAPTable_Object=MibTable
qtechStaAssRecordsSearchByAPTable=_QtechStaAssRecordsSearchByAPTable_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1))
if mibBuilder.loadTexts:qtechStaAssRecordsSearchByAPTable.setStatus(_A)
_QtechStaAssRecordsSearchByAPEntry_Object=MibTableRow
qtechStaAssRecordsSearchByAPEntry=_QtechStaAssRecordsSearchByAPEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1))
qtechStaAssRecordsSearchByAPEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:qtechStaAssRecordsSearchByAPEntry.setStatus(_A)
class _QtechStaAPAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechStaAPAPName_Type.__name__=_E
_QtechStaAPAPName_Object=MibTableColumn
qtechStaAPAPName=_QtechStaAPAPName_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,1),_QtechStaAPAPName_Type())
qtechStaAPAPName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaAPAPName.setStatus(_A)
_QtechStaAPindex_Type=Unsigned32
_QtechStaAPindex_Object=MibTableColumn
qtechStaAPindex=_QtechStaAPindex_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,2),_QtechStaAPindex_Type())
qtechStaAPindex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaAPindex.setStatus(_A)
_QtechStaAPMac_Type=MacAddress
_QtechStaAPMac_Object=MibTableColumn
qtechStaAPMac=_QtechStaAPMac_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,3),_QtechStaAPMac_Type())
qtechStaAPMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPMac.setStatus(_A)
class _QtechStaAPISUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_QtechStaAPISUP_Type.__name__=_F
_QtechStaAPISUP_Object=MibTableColumn
qtechStaAPISUP=_QtechStaAPISUP_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,4),_QtechStaAPISUP_Type())
qtechStaAPISUP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPISUP.setStatus(_A)
_QtechStaAPStartime_Type=DateAndTime
_QtechStaAPStartime_Object=MibTableColumn
qtechStaAPStartime=_QtechStaAPStartime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,5),_QtechStaAPStartime_Type())
qtechStaAPStartime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPStartime.setStatus(_A)
_QtechStaAPupdowntimes_Type=Unsigned32
_QtechStaAPupdowntimes_Object=MibTableColumn
qtechStaAPupdowntimes=_QtechStaAPupdowntimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,6),_QtechStaAPupdowntimes_Type())
qtechStaAPupdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPupdowntimes.setStatus(_A)
_QtechStaAProamtimes_Type=Unsigned32
_QtechStaAProamtimes_Object=MibTableColumn
qtechStaAProamtimes=_QtechStaAProamtimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,7),_QtechStaAProamtimes_Type())
qtechStaAProamtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAProamtimes.setStatus(_A)
_QtechStaAPtotaltimes_Type=Unsigned32
_QtechStaAPtotaltimes_Object=MibTableColumn
qtechStaAPtotaltimes=_QtechStaAPtotaltimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,8),_QtechStaAPtotaltimes_Type())
qtechStaAPtotaltimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPtotaltimes.setStatus(_A)
_QtechStaAPjitter_Type=Integer32
_QtechStaAPjitter_Object=MibTableColumn
qtechStaAPjitter=_QtechStaAPjitter_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,9),_QtechStaAPjitter_Type())
qtechStaAPjitter.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPjitter.setStatus(_A)
_QtechStaAPjointimes_Type=Unsigned32
_QtechStaAPjointimes_Object=MibTableColumn
qtechStaAPjointimes=_QtechStaAPjointimes_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,10),_QtechStaAPjointimes_Type())
qtechStaAPjointimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPjointimes.setStatus(_A)
_QtechStaAPlatelytime_Type=DateAndTime
_QtechStaAPlatelytime_Object=MibTableColumn
qtechStaAPlatelytime=_QtechStaAPlatelytime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,11),_QtechStaAPlatelytime_Type())
qtechStaAPlatelytime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPlatelytime.setStatus(_A)
_QtechStaAPSSID_Type=DisplayString
_QtechStaAPSSID_Object=MibTableColumn
qtechStaAPSSID=_QtechStaAPSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,4,1,1,12),_QtechStaAPSSID_Type())
qtechStaAPSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaAPSSID.setStatus(_A)
_QtechStaAssSignalByMAC_ObjectIdentity=ObjectIdentity
qtechStaAssSignalByMAC=_QtechStaAssSignalByMAC_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,5))
_QtechStaAssSignalByMACTable_Object=MibTable
qtechStaAssSignalByMACTable=_QtechStaAssSignalByMACTable_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,5,1))
if mibBuilder.loadTexts:qtechStaAssSignalByMACTable.setStatus(_A)
_QtechStaAssSignalByMACEntry_Object=MibTableRow
qtechStaAssSignalByMACEntry=_QtechStaAssSignalByMACEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,5,1,1))
qtechStaAssSignalByMACEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:qtechStaAssSignalByMACEntry.setStatus(_A)
_QtechStaSignalMacAddress_Type=MacAddress
_QtechStaSignalMacAddress_Object=MibTableColumn
qtechStaSignalMacAddress=_QtechStaSignalMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,5,1,1,1),_QtechStaSignalMacAddress_Type())
qtechStaSignalMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaSignalMacAddress.setStatus(_A)
_QtechStaSignalMacindex_Type=Unsigned32
_QtechStaSignalMacindex_Object=MibTableColumn
qtechStaSignalMacindex=_QtechStaSignalMacindex_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,5,1,1,2),_QtechStaSignalMacindex_Type())
qtechStaSignalMacindex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaSignalMacindex.setStatus(_A)
_QtechStaSignaltime_Type=DateAndTime
_QtechStaSignaltime_Object=MibTableColumn
qtechStaSignaltime=_QtechStaSignaltime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,5,1,1,3),_QtechStaSignaltime_Type())
qtechStaSignaltime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaSignaltime.setStatus(_A)
_QtechStaSignalValue_Type=Integer32
_QtechStaSignalValue_Object=MibTableColumn
qtechStaSignalValue=_QtechStaSignalValue_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,5,1,1,4),_QtechStaSignalValue_Type())
qtechStaSignalValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaSignalValue.setStatus(_A)
_QtechStaAssRetryByMAC_ObjectIdentity=ObjectIdentity
qtechStaAssRetryByMAC=_QtechStaAssRetryByMAC_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,6))
_QtechStaAssRetryByMACTable_Object=MibTable
qtechStaAssRetryByMACTable=_QtechStaAssRetryByMACTable_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,6,1))
if mibBuilder.loadTexts:qtechStaAssRetryByMACTable.setStatus(_A)
_QtechStaAssRetryByMACEntry_Object=MibTableRow
qtechStaAssRetryByMACEntry=_QtechStaAssRetryByMACEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,6,1,1))
qtechStaAssRetryByMACEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:qtechStaAssRetryByMACEntry.setStatus(_A)
_QtechStaRetryMacAddress_Type=MacAddress
_QtechStaRetryMacAddress_Object=MibTableColumn
qtechStaRetryMacAddress=_QtechStaRetryMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,6,1,1,1),_QtechStaRetryMacAddress_Type())
qtechStaRetryMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaRetryMacAddress.setStatus(_A)
_QtechStaRetryMacindex_Type=Unsigned32
_QtechStaRetryMacindex_Object=MibTableColumn
qtechStaRetryMacindex=_QtechStaRetryMacindex_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,6,1,1,2),_QtechStaRetryMacindex_Type())
qtechStaRetryMacindex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechStaRetryMacindex.setStatus(_A)
_QtechStaRetrytime_Type=DateAndTime
_QtechStaRetrytime_Object=MibTableColumn
qtechStaRetrytime=_QtechStaRetrytime_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,6,1,1,3),_QtechStaRetrytime_Type())
qtechStaRetrytime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaRetrytime.setStatus(_A)
_QtechStaRetryValue_Type=Integer32
_QtechStaRetryValue_Object=MibTableColumn
qtechStaRetryValue=_QtechStaRetryValue_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,6,1,1,4),_QtechStaRetryValue_Type())
qtechStaRetryValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechStaRetryValue.setStatus(_A)
_QtechStaAssStatistic_ObjectIdentity=ObjectIdentity
qtechStaAssStatistic=_QtechStaAssStatistic_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,1,7))
_QtechAssStatisticsTotalsta_Type=Unsigned32
_QtechAssStatisticsTotalsta_Object=MibScalar
qtechAssStatisticsTotalsta=_QtechAssStatisticsTotalsta_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,7,1),_QtechAssStatisticsTotalsta_Type())
qtechAssStatisticsTotalsta.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAssStatisticsTotalsta.setStatus(_A)
_QtechAssStatisticsTotalinfo_Type=Unsigned32
_QtechAssStatisticsTotalinfo_Object=MibScalar
qtechAssStatisticsTotalinfo=_QtechAssStatisticsTotalinfo_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,7,2),_QtechAssStatisticsTotalinfo_Type())
qtechAssStatisticsTotalinfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAssStatisticsTotalinfo.setStatus(_A)
_QtechAssStatisticsdown_Type=Unsigned32
_QtechAssStatisticsdown_Object=MibScalar
qtechAssStatisticsdown=_QtechAssStatisticsdown_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,7,3),_QtechAssStatisticsdown_Type())
qtechAssStatisticsdown.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAssStatisticsdown.setStatus(_A)
_QtechAssStatisticsObligate1_Type=Unsigned32
_QtechAssStatisticsObligate1_Object=MibScalar
qtechAssStatisticsObligate1=_QtechAssStatisticsObligate1_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,7,4),_QtechAssStatisticsObligate1_Type())
qtechAssStatisticsObligate1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAssStatisticsObligate1.setStatus(_A)
_QtechAssStatisticsObligate2_Type=Unsigned32
_QtechAssStatisticsObligate2_Object=MibScalar
qtechAssStatisticsObligate2=_QtechAssStatisticsObligate2_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,7,5),_QtechAssStatisticsObligate2_Type())
qtechAssStatisticsObligate2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAssStatisticsObligate2.setStatus(_A)
_QtechAssStatisticsObligate3_Type=Unsigned32
_QtechAssStatisticsObligate3_Object=MibScalar
qtechAssStatisticsObligate3=_QtechAssStatisticsObligate3_Object((1,3,6,1,4,1,27514,1,1,10,2,101,1,7,6),_QtechAssStatisticsObligate3_Type())
qtechAssStatisticsObligate3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAssStatisticsObligate3.setStatus(_A)
_QtechStaAssRecordsMIBConformance_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsMIBConformance=_QtechStaAssRecordsMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,2))
_QtechStaAssRecordsMIBCompliances_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsMIBCompliances=_QtechStaAssRecordsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,2,1))
_QtechStaAssRecordsMIBGroups_ObjectIdentity=ObjectIdentity
qtechStaAssRecordsMIBGroups=_QtechStaAssRecordsMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,101,2,2))
qtechStaAssRecordsGrobalMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,1))
qtechStaAssRecordsGrobalMIBroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:qtechStaAssRecordsGrobalMIBroup.setStatus(_A)
qtechStaAssRecordsMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,2))
qtechStaAssRecordsMIBroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:qtechStaAssRecordsMIBroup.setStatus(_A)
qtechStaAssRecordsSearchByTimeMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,3))
qtechStaAssRecordsSearchByTimeMIBroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:qtechStaAssRecordsSearchByTimeMIBroup.setStatus(_A)
qtechStaAssRecordsSearchByAPMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,4))
qtechStaAssRecordsSearchByAPMIBroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:qtechStaAssRecordsSearchByAPMIBroup.setStatus(_A)
qtechStaAssSignalSearchByMACMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,5))
qtechStaAssSignalSearchByMACMIBroup.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:qtechStaAssSignalSearchByMACMIBroup.setStatus(_A)
qtechStaAssRetrySearchByMACMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,6))
qtechStaAssRetrySearchByMACMIBroup.setObjects(*((_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:qtechStaAssRetrySearchByMACMIBroup.setStatus(_A)
qtechStaAssStatisticsMIBroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,101,2,2,7))
qtechStaAssStatisticsMIBroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:qtechStaAssStatisticsMIBroup.setStatus(_A)
qtechStaAssRecordsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,101,2,1,1))
qtechStaAssRecordsMIBCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:qtechStaAssRecordsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechStaAssRecordsMIB':qtechStaAssRecordsMIB,'qtechStaAssRecordsMIBTrap':qtechStaAssRecordsMIBTrap,'qtechStaAssRecordsMIBObjects':qtechStaAssRecordsMIBObjects,'qtechStaAssRecordsGrobal':qtechStaAssRecordsGrobal,'qtechStaAssRecordsGrobalTable':qtechStaAssRecordsGrobalTable,'qtechStaAssRecordsGrobalEntry':qtechStaAssRecordsGrobalEntry,_H:qtechStaMacGrobalAddress,_V:qtechStaMacGrobalAPName,_W:qtechStaMacGrobalISUP,_X:qtechStaMacGrobalStartime,_Y:qtechStaMacGrobalupdowntimes,_Z:qtechStaMacGrobalroamtimes,_a:qtechStaMacGrobaltotaltimes,_b:qtechStaMacGrobalrealdowntimes,_c:qtechStaMacGrobalSSID,'qtechStaAssRecordsByMAC':qtechStaAssRecordsByMAC,'qtechStaAssRecordsByMACTable':qtechStaAssRecordsByMACTable,'qtechStaAssRecordsByMACEntry':qtechStaAssRecordsByMACEntry,_I:qtechStaMacAddress,_J:qtechStaMacindex,_d:qtechStaAsstime,_e:qtechStaAssAction,_f:qtechStaAssSubAction,_g:qtechStaAssResult,_h:qtechStaAssReason,_i:qtechStaAssApNamePre,_j:qtechStaAssApNameNow,_k:qtechStaAssSignalQua,_l:qtechStaAssRoamtype,_m:qtechStaAssjitter,_n:qtechStaAssjointimes,_o:qtechStaAsslatelytime,_p:qtechStaAssSSID,'qtechStaAssRecordsByTime':qtechStaAssRecordsByTime,'qtechStaAssRecordsSearchByTimeTable':qtechStaAssRecordsSearchByTimeTable,'qtechStaAssRecordsSearchByTimeEntry':qtechStaAssRecordsSearchByTimeEntry,_K:qtechStaUptimeLow,_L:qtechStaUptimeHigh,_M:qtechStaDowntimeLow,_N:qtechStaDowntimeHigh,_O:qtechStaTimeindex,_q:qtechStaTimeMac,_r:qtechStaTimeAPName,_s:qtechStaTimeISUP,_t:qtechStaTimeStartime,_u:qtechStaTimeupdowntimes,_v:qtechStaTimeroamtimes,_w:qtechStaTimertotaltimes,_x:qtechStaTimerjitter,_y:qtechStaTimerjointimes,_z:qtechStaTimerlatelytime,_A0:qtechStaTimerSSID,'qtechStaAssRecordsByAP':qtechStaAssRecordsByAP,'qtechStaAssRecordsSearchByAPTable':qtechStaAssRecordsSearchByAPTable,'qtechStaAssRecordsSearchByAPEntry':qtechStaAssRecordsSearchByAPEntry,_P:qtechStaAPAPName,_Q:qtechStaAPindex,_A1:qtechStaAPMac,_A2:qtechStaAPISUP,_A3:qtechStaAPStartime,_A4:qtechStaAPupdowntimes,_A5:qtechStaAProamtimes,_A6:qtechStaAPtotaltimes,_A7:qtechStaAPjitter,_A8:qtechStaAPjointimes,_A9:qtechStaAPlatelytime,_AA:qtechStaAPSSID,'qtechStaAssSignalByMAC':qtechStaAssSignalByMAC,'qtechStaAssSignalByMACTable':qtechStaAssSignalByMACTable,'qtechStaAssSignalByMACEntry':qtechStaAssSignalByMACEntry,_R:qtechStaSignalMacAddress,_S:qtechStaSignalMacindex,_AB:qtechStaSignaltime,_AC:qtechStaSignalValue,'qtechStaAssRetryByMAC':qtechStaAssRetryByMAC,'qtechStaAssRetryByMACTable':qtechStaAssRetryByMACTable,'qtechStaAssRetryByMACEntry':qtechStaAssRetryByMACEntry,_T:qtechStaRetryMacAddress,_U:qtechStaRetryMacindex,_AD:qtechStaRetrytime,_AE:qtechStaRetryValue,'qtechStaAssStatistic':qtechStaAssStatistic,_AF:qtechAssStatisticsTotalsta,_AG:qtechAssStatisticsTotalinfo,_AH:qtechAssStatisticsdown,_AI:qtechAssStatisticsObligate1,_AJ:qtechAssStatisticsObligate2,_AK:qtechAssStatisticsObligate3,'qtechStaAssRecordsMIBConformance':qtechStaAssRecordsMIBConformance,'qtechStaAssRecordsMIBCompliances':qtechStaAssRecordsMIBCompliances,'qtechStaAssRecordsMIBCompliance':qtechStaAssRecordsMIBCompliance,'qtechStaAssRecordsMIBGroups':qtechStaAssRecordsMIBGroups,_AL:qtechStaAssRecordsGrobalMIBroup,_AM:qtechStaAssRecordsMIBroup,_AN:qtechStaAssRecordsSearchByTimeMIBroup,_AO:qtechStaAssRecordsSearchByAPMIBroup,_AP:qtechStaAssSignalSearchByMACMIBroup,_AQ:qtechStaAssRetrySearchByMACMIBroup,_AR:qtechStaAssStatisticsMIBroup})