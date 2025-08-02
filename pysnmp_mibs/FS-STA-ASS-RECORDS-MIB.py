_AR='fsStaAssStatisticsMIBroup'
_AQ='fsStaAssRetrySearchByMACMIBroup'
_AP='fsStaAssSignalSearchByMACMIBroup'
_AO='fsStaAssRecordsSearchByAPMIBroup'
_AN='fsStaAssRecordsSearchByTimeMIBroup'
_AM='fsStaAssRecordsMIBroup'
_AL='fsStaAssRecordsGrobalMIBroup'
_AK='fsAssStatisticsObligate3'
_AJ='fsAssStatisticsObligate2'
_AI='fsAssStatisticsObligate1'
_AH='fsAssStatisticsdown'
_AG='fsAssStatisticsTotalinfo'
_AF='fsAssStatisticsTotalsta'
_AE='fsStaRetryValue'
_AD='fsStaRetrytime'
_AC='fsStaSignalValue'
_AB='fsStaSignaltime'
_AA='fsStaAPSSID'
_A9='fsStaAPlatelytime'
_A8='fsStaAPjointimes'
_A7='fsStaAPjitter'
_A6='fsStaAPtotaltimes'
_A5='fsStaAProamtimes'
_A4='fsStaAPupdowntimes'
_A3='fsStaAPStartime'
_A2='fsStaAPISUP'
_A1='fsStaAPMac'
_A0='fsStaTimerSSID'
_z='fsStaTimerlatelytime'
_y='fsStaTimerjointimes'
_x='fsStaTimerjitter'
_w='fsStaTimertotaltimes'
_v='fsStaTimeroamtimes'
_u='fsStaTimeupdowntimes'
_t='fsStaTimeStartime'
_s='fsStaTimeISUP'
_r='fsStaTimeAPName'
_q='fsStaTimeMac'
_p='fsStaAssSSID'
_o='fsStaAsslatelytime'
_n='fsStaAssjointimes'
_m='fsStaAssjitter'
_l='fsStaAssRoamtype'
_k='fsStaAssSignalQua'
_j='fsStaAssApNameNow'
_i='fsStaAssApNamePre'
_h='fsStaAssReason'
_g='fsStaAssResult'
_f='fsStaAssSubAction'
_e='fsStaAssAction'
_d='fsStaAsstime'
_c='fsStaMacGrobalSSID'
_b='fsStaMacGrobalrealdowntimes'
_a='fsStaMacGrobaltotaltimes'
_Z='fsStaMacGrobalroamtimes'
_Y='fsStaMacGrobalupdowntimes'
_X='fsStaMacGrobalStartime'
_W='fsStaMacGrobalISUP'
_V='fsStaMacGrobalAPName'
_U='fsStaRetryMacindex'
_T='fsStaRetryMacAddress'
_S='fsStaSignalMacindex'
_R='fsStaSignalMacAddress'
_Q='fsStaAPindex'
_P='fsStaAPAPName'
_O='fsStaTimeindex'
_N='fsStaDowntimeHigh'
_M='fsStaDowntimeLow'
_L='fsStaUptimeHigh'
_K='fsStaUptimeLow'
_J='fsStaMacindex'
_I='fsStaMacAddress'
_H='fsStaMacGrobalAddress'
_G='down'
_F='Integer32'
_E='DisplayString'
_D='not-accessible'
_C='read-only'
_B='FS-STA-ASS-RECORDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsIfIndex,=mibBuilder.importSymbols('FS-INTERFACE-MIB','fsIfIndex')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsStaAssRecordsMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,101))
if mibBuilder.loadTexts:fsStaAssRecordsMIB.setRevisions(('2009-11-10 00:00',))
_FsStaAssRecordsMIBTrap_ObjectIdentity=ObjectIdentity
fsStaAssRecordsMIBTrap=_FsStaAssRecordsMIBTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,0))
_FsStaAssRecordsMIBObjects_ObjectIdentity=ObjectIdentity
fsStaAssRecordsMIBObjects=_FsStaAssRecordsMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1))
_FsStaAssRecordsGrobal_ObjectIdentity=ObjectIdentity
fsStaAssRecordsGrobal=_FsStaAssRecordsGrobal_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,1))
_FsStaAssRecordsGrobalTable_Object=MibTable
fsStaAssRecordsGrobalTable=_FsStaAssRecordsGrobalTable_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1))
if mibBuilder.loadTexts:fsStaAssRecordsGrobalTable.setStatus(_A)
_FsStaAssRecordsGrobalEntry_Object=MibTableRow
fsStaAssRecordsGrobalEntry=_FsStaAssRecordsGrobalEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1))
fsStaAssRecordsGrobalEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsStaAssRecordsGrobalEntry.setStatus(_A)
_FsStaMacGrobalAddress_Type=MacAddress
_FsStaMacGrobalAddress_Object=MibTableColumn
fsStaMacGrobalAddress=_FsStaMacGrobalAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,1),_FsStaMacGrobalAddress_Type())
fsStaMacGrobalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaMacGrobalAddress.setStatus(_A)
class _FsStaMacGrobalAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsStaMacGrobalAPName_Type.__name__=_E
_FsStaMacGrobalAPName_Object=MibTableColumn
fsStaMacGrobalAPName=_FsStaMacGrobalAPName_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,2),_FsStaMacGrobalAPName_Type())
fsStaMacGrobalAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalAPName.setStatus(_A)
class _FsStaMacGrobalISUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_FsStaMacGrobalISUP_Type.__name__=_F
_FsStaMacGrobalISUP_Object=MibTableColumn
fsStaMacGrobalISUP=_FsStaMacGrobalISUP_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,3),_FsStaMacGrobalISUP_Type())
fsStaMacGrobalISUP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalISUP.setStatus(_A)
_FsStaMacGrobalStartime_Type=DateAndTime
_FsStaMacGrobalStartime_Object=MibTableColumn
fsStaMacGrobalStartime=_FsStaMacGrobalStartime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,4),_FsStaMacGrobalStartime_Type())
fsStaMacGrobalStartime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalStartime.setStatus(_A)
_FsStaMacGrobalupdowntimes_Type=Unsigned32
_FsStaMacGrobalupdowntimes_Object=MibTableColumn
fsStaMacGrobalupdowntimes=_FsStaMacGrobalupdowntimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,5),_FsStaMacGrobalupdowntimes_Type())
fsStaMacGrobalupdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalupdowntimes.setStatus(_A)
_FsStaMacGrobalroamtimes_Type=Unsigned32
_FsStaMacGrobalroamtimes_Object=MibTableColumn
fsStaMacGrobalroamtimes=_FsStaMacGrobalroamtimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,6),_FsStaMacGrobalroamtimes_Type())
fsStaMacGrobalroamtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalroamtimes.setStatus(_A)
_FsStaMacGrobaltotaltimes_Type=Unsigned32
_FsStaMacGrobaltotaltimes_Object=MibTableColumn
fsStaMacGrobaltotaltimes=_FsStaMacGrobaltotaltimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,7),_FsStaMacGrobaltotaltimes_Type())
fsStaMacGrobaltotaltimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobaltotaltimes.setStatus(_A)
_FsStaMacGrobalrealdowntimes_Type=Unsigned32
_FsStaMacGrobalrealdowntimes_Object=MibTableColumn
fsStaMacGrobalrealdowntimes=_FsStaMacGrobalrealdowntimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,8),_FsStaMacGrobalrealdowntimes_Type())
fsStaMacGrobalrealdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalrealdowntimes.setStatus(_A)
class _FsStaMacGrobalSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsStaMacGrobalSSID_Type.__name__=_E
_FsStaMacGrobalSSID_Object=MibTableColumn
fsStaMacGrobalSSID=_FsStaMacGrobalSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,1,1,1,9),_FsStaMacGrobalSSID_Type())
fsStaMacGrobalSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaMacGrobalSSID.setStatus(_A)
_FsStaAssRecordsByMAC_ObjectIdentity=ObjectIdentity
fsStaAssRecordsByMAC=_FsStaAssRecordsByMAC_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,2))
_FsStaAssRecordsByMACTable_Object=MibTable
fsStaAssRecordsByMACTable=_FsStaAssRecordsByMACTable_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1))
if mibBuilder.loadTexts:fsStaAssRecordsByMACTable.setStatus(_A)
_FsStaAssRecordsByMACEntry_Object=MibTableRow
fsStaAssRecordsByMACEntry=_FsStaAssRecordsByMACEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1))
fsStaAssRecordsByMACEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:fsStaAssRecordsByMACEntry.setStatus(_A)
_FsStaMacAddress_Type=MacAddress
_FsStaMacAddress_Object=MibTableColumn
fsStaMacAddress=_FsStaMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,1),_FsStaMacAddress_Type())
fsStaMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaMacAddress.setStatus(_A)
_FsStaMacindex_Type=Unsigned32
_FsStaMacindex_Object=MibTableColumn
fsStaMacindex=_FsStaMacindex_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,2),_FsStaMacindex_Type())
fsStaMacindex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaMacindex.setStatus(_A)
_FsStaAsstime_Type=DateAndTime
_FsStaAsstime_Object=MibTableColumn
fsStaAsstime=_FsStaAsstime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,3),_FsStaAsstime_Type())
fsStaAsstime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAsstime.setStatus(_A)
class _FsStaAssAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('join',1),('leave',2),('roam',3),('delete',4)))
_FsStaAssAction_Type.__name__=_F
_FsStaAssAction_Object=MibTableColumn
fsStaAssAction=_FsStaAssAction_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,4),_FsStaAssAction_Type())
fsStaAssAction.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssAction.setStatus(_A)
_FsStaAssSubAction_Type=Integer32
_FsStaAssSubAction_Object=MibTableColumn
fsStaAssSubAction=_FsStaAssSubAction_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,5),_FsStaAssSubAction_Type())
fsStaAssSubAction.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssSubAction.setStatus(_A)
class _FsStaAssResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('success',0),('failed',1)))
_FsStaAssResult_Type.__name__=_F
_FsStaAssResult_Object=MibTableColumn
fsStaAssResult=_FsStaAssResult_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,6),_FsStaAssResult_Type())
fsStaAssResult.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssResult.setStatus(_A)
_FsStaAssReason_Type=Integer32
_FsStaAssReason_Object=MibTableColumn
fsStaAssReason=_FsStaAssReason_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,7),_FsStaAssReason_Type())
fsStaAssReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssReason.setStatus(_A)
class _FsStaAssApNamePre_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsStaAssApNamePre_Type.__name__=_E
_FsStaAssApNamePre_Object=MibTableColumn
fsStaAssApNamePre=_FsStaAssApNamePre_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,8),_FsStaAssApNamePre_Type())
fsStaAssApNamePre.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssApNamePre.setStatus(_A)
class _FsStaAssApNameNow_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsStaAssApNameNow_Type.__name__=_E
_FsStaAssApNameNow_Object=MibTableColumn
fsStaAssApNameNow=_FsStaAssApNameNow_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,9),_FsStaAssApNameNow_Type())
fsStaAssApNameNow.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssApNameNow.setStatus(_A)
_FsStaAssSignalQua_Type=Integer32
_FsStaAssSignalQua_Object=MibTableColumn
fsStaAssSignalQua=_FsStaAssSignalQua_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,10),_FsStaAssSignalQua_Type())
fsStaAssSignalQua.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssSignalQua.setStatus(_A)
_FsStaAssRoamtype_Type=Integer32
_FsStaAssRoamtype_Object=MibTableColumn
fsStaAssRoamtype=_FsStaAssRoamtype_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,11),_FsStaAssRoamtype_Type())
fsStaAssRoamtype.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssRoamtype.setStatus(_A)
_FsStaAssjitter_Type=Integer32
_FsStaAssjitter_Object=MibTableColumn
fsStaAssjitter=_FsStaAssjitter_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,12),_FsStaAssjitter_Type())
fsStaAssjitter.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssjitter.setStatus(_A)
_FsStaAssjointimes_Type=Unsigned32
_FsStaAssjointimes_Object=MibTableColumn
fsStaAssjointimes=_FsStaAssjointimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,13),_FsStaAssjointimes_Type())
fsStaAssjointimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssjointimes.setStatus(_A)
_FsStaAsslatelytime_Type=DateAndTime
_FsStaAsslatelytime_Object=MibTableColumn
fsStaAsslatelytime=_FsStaAsslatelytime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,14),_FsStaAsslatelytime_Type())
fsStaAsslatelytime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAsslatelytime.setStatus(_A)
_FsStaAssSSID_Type=DisplayString
_FsStaAssSSID_Object=MibTableColumn
fsStaAssSSID=_FsStaAssSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,2,1,1,15),_FsStaAssSSID_Type())
fsStaAssSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAssSSID.setStatus(_A)
_FsStaAssRecordsByTime_ObjectIdentity=ObjectIdentity
fsStaAssRecordsByTime=_FsStaAssRecordsByTime_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,3))
_FsStaAssRecordsSearchByTimeTable_Object=MibTable
fsStaAssRecordsSearchByTimeTable=_FsStaAssRecordsSearchByTimeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1))
if mibBuilder.loadTexts:fsStaAssRecordsSearchByTimeTable.setStatus(_A)
_FsStaAssRecordsSearchByTimeEntry_Object=MibTableRow
fsStaAssRecordsSearchByTimeEntry=_FsStaAssRecordsSearchByTimeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1))
fsStaAssRecordsSearchByTimeEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:fsStaAssRecordsSearchByTimeEntry.setStatus(_A)
_FsStaUptimeLow_Type=DateAndTime
_FsStaUptimeLow_Object=MibTableColumn
fsStaUptimeLow=_FsStaUptimeLow_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,1),_FsStaUptimeLow_Type())
fsStaUptimeLow.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaUptimeLow.setStatus(_A)
_FsStaUptimeHigh_Type=DateAndTime
_FsStaUptimeHigh_Object=MibTableColumn
fsStaUptimeHigh=_FsStaUptimeHigh_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,2),_FsStaUptimeHigh_Type())
fsStaUptimeHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaUptimeHigh.setStatus(_A)
_FsStaDowntimeLow_Type=DateAndTime
_FsStaDowntimeLow_Object=MibTableColumn
fsStaDowntimeLow=_FsStaDowntimeLow_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,3),_FsStaDowntimeLow_Type())
fsStaDowntimeLow.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaDowntimeLow.setStatus(_A)
_FsStaDowntimeHigh_Type=DateAndTime
_FsStaDowntimeHigh_Object=MibTableColumn
fsStaDowntimeHigh=_FsStaDowntimeHigh_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,4),_FsStaDowntimeHigh_Type())
fsStaDowntimeHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaDowntimeHigh.setStatus(_A)
_FsStaTimeindex_Type=Unsigned32
_FsStaTimeindex_Object=MibTableColumn
fsStaTimeindex=_FsStaTimeindex_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,5),_FsStaTimeindex_Type())
fsStaTimeindex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaTimeindex.setStatus(_A)
_FsStaTimeMac_Type=MacAddress
_FsStaTimeMac_Object=MibTableColumn
fsStaTimeMac=_FsStaTimeMac_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,6),_FsStaTimeMac_Type())
fsStaTimeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimeMac.setStatus(_A)
class _FsStaTimeAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsStaTimeAPName_Type.__name__=_E
_FsStaTimeAPName_Object=MibTableColumn
fsStaTimeAPName=_FsStaTimeAPName_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,7),_FsStaTimeAPName_Type())
fsStaTimeAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimeAPName.setStatus(_A)
class _FsStaTimeISUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_FsStaTimeISUP_Type.__name__=_F
_FsStaTimeISUP_Object=MibTableColumn
fsStaTimeISUP=_FsStaTimeISUP_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,8),_FsStaTimeISUP_Type())
fsStaTimeISUP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimeISUP.setStatus(_A)
_FsStaTimeStartime_Type=DateAndTime
_FsStaTimeStartime_Object=MibTableColumn
fsStaTimeStartime=_FsStaTimeStartime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,9),_FsStaTimeStartime_Type())
fsStaTimeStartime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimeStartime.setStatus(_A)
_FsStaTimeupdowntimes_Type=Unsigned32
_FsStaTimeupdowntimes_Object=MibTableColumn
fsStaTimeupdowntimes=_FsStaTimeupdowntimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,10),_FsStaTimeupdowntimes_Type())
fsStaTimeupdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimeupdowntimes.setStatus(_A)
_FsStaTimeroamtimes_Type=Unsigned32
_FsStaTimeroamtimes_Object=MibTableColumn
fsStaTimeroamtimes=_FsStaTimeroamtimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,11),_FsStaTimeroamtimes_Type())
fsStaTimeroamtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimeroamtimes.setStatus(_A)
_FsStaTimertotaltimes_Type=Unsigned32
_FsStaTimertotaltimes_Object=MibTableColumn
fsStaTimertotaltimes=_FsStaTimertotaltimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,12),_FsStaTimertotaltimes_Type())
fsStaTimertotaltimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimertotaltimes.setStatus(_A)
_FsStaTimerjitter_Type=Integer32
_FsStaTimerjitter_Object=MibTableColumn
fsStaTimerjitter=_FsStaTimerjitter_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,13),_FsStaTimerjitter_Type())
fsStaTimerjitter.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimerjitter.setStatus(_A)
_FsStaTimerjointimes_Type=Unsigned32
_FsStaTimerjointimes_Object=MibTableColumn
fsStaTimerjointimes=_FsStaTimerjointimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,14),_FsStaTimerjointimes_Type())
fsStaTimerjointimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimerjointimes.setStatus(_A)
_FsStaTimerlatelytime_Type=DateAndTime
_FsStaTimerlatelytime_Object=MibTableColumn
fsStaTimerlatelytime=_FsStaTimerlatelytime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,15),_FsStaTimerlatelytime_Type())
fsStaTimerlatelytime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimerlatelytime.setStatus(_A)
_FsStaTimerSSID_Type=DisplayString
_FsStaTimerSSID_Object=MibTableColumn
fsStaTimerSSID=_FsStaTimerSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,3,1,1,16),_FsStaTimerSSID_Type())
fsStaTimerSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaTimerSSID.setStatus(_A)
_FsStaAssRecordsByAP_ObjectIdentity=ObjectIdentity
fsStaAssRecordsByAP=_FsStaAssRecordsByAP_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,4))
_FsStaAssRecordsSearchByAPTable_Object=MibTable
fsStaAssRecordsSearchByAPTable=_FsStaAssRecordsSearchByAPTable_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1))
if mibBuilder.loadTexts:fsStaAssRecordsSearchByAPTable.setStatus(_A)
_FsStaAssRecordsSearchByAPEntry_Object=MibTableRow
fsStaAssRecordsSearchByAPEntry=_FsStaAssRecordsSearchByAPEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1))
fsStaAssRecordsSearchByAPEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:fsStaAssRecordsSearchByAPEntry.setStatus(_A)
class _FsStaAPAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsStaAPAPName_Type.__name__=_E
_FsStaAPAPName_Object=MibTableColumn
fsStaAPAPName=_FsStaAPAPName_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,1),_FsStaAPAPName_Type())
fsStaAPAPName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaAPAPName.setStatus(_A)
_FsStaAPindex_Type=Unsigned32
_FsStaAPindex_Object=MibTableColumn
fsStaAPindex=_FsStaAPindex_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,2),_FsStaAPindex_Type())
fsStaAPindex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaAPindex.setStatus(_A)
_FsStaAPMac_Type=MacAddress
_FsStaAPMac_Object=MibTableColumn
fsStaAPMac=_FsStaAPMac_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,3),_FsStaAPMac_Type())
fsStaAPMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPMac.setStatus(_A)
class _FsStaAPISUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('up',0),(_G,1)))
_FsStaAPISUP_Type.__name__=_F
_FsStaAPISUP_Object=MibTableColumn
fsStaAPISUP=_FsStaAPISUP_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,4),_FsStaAPISUP_Type())
fsStaAPISUP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPISUP.setStatus(_A)
_FsStaAPStartime_Type=DateAndTime
_FsStaAPStartime_Object=MibTableColumn
fsStaAPStartime=_FsStaAPStartime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,5),_FsStaAPStartime_Type())
fsStaAPStartime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPStartime.setStatus(_A)
_FsStaAPupdowntimes_Type=Unsigned32
_FsStaAPupdowntimes_Object=MibTableColumn
fsStaAPupdowntimes=_FsStaAPupdowntimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,6),_FsStaAPupdowntimes_Type())
fsStaAPupdowntimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPupdowntimes.setStatus(_A)
_FsStaAProamtimes_Type=Unsigned32
_FsStaAProamtimes_Object=MibTableColumn
fsStaAProamtimes=_FsStaAProamtimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,7),_FsStaAProamtimes_Type())
fsStaAProamtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAProamtimes.setStatus(_A)
_FsStaAPtotaltimes_Type=Unsigned32
_FsStaAPtotaltimes_Object=MibTableColumn
fsStaAPtotaltimes=_FsStaAPtotaltimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,8),_FsStaAPtotaltimes_Type())
fsStaAPtotaltimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPtotaltimes.setStatus(_A)
_FsStaAPjitter_Type=Integer32
_FsStaAPjitter_Object=MibTableColumn
fsStaAPjitter=_FsStaAPjitter_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,9),_FsStaAPjitter_Type())
fsStaAPjitter.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPjitter.setStatus(_A)
_FsStaAPjointimes_Type=Unsigned32
_FsStaAPjointimes_Object=MibTableColumn
fsStaAPjointimes=_FsStaAPjointimes_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,10),_FsStaAPjointimes_Type())
fsStaAPjointimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPjointimes.setStatus(_A)
_FsStaAPlatelytime_Type=DateAndTime
_FsStaAPlatelytime_Object=MibTableColumn
fsStaAPlatelytime=_FsStaAPlatelytime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,11),_FsStaAPlatelytime_Type())
fsStaAPlatelytime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPlatelytime.setStatus(_A)
_FsStaAPSSID_Type=DisplayString
_FsStaAPSSID_Object=MibTableColumn
fsStaAPSSID=_FsStaAPSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,4,1,1,12),_FsStaAPSSID_Type())
fsStaAPSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaAPSSID.setStatus(_A)
_FsStaAssSignalByMAC_ObjectIdentity=ObjectIdentity
fsStaAssSignalByMAC=_FsStaAssSignalByMAC_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,5))
_FsStaAssSignalByMACTable_Object=MibTable
fsStaAssSignalByMACTable=_FsStaAssSignalByMACTable_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,5,1))
if mibBuilder.loadTexts:fsStaAssSignalByMACTable.setStatus(_A)
_FsStaAssSignalByMACEntry_Object=MibTableRow
fsStaAssSignalByMACEntry=_FsStaAssSignalByMACEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,5,1,1))
fsStaAssSignalByMACEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:fsStaAssSignalByMACEntry.setStatus(_A)
_FsStaSignalMacAddress_Type=MacAddress
_FsStaSignalMacAddress_Object=MibTableColumn
fsStaSignalMacAddress=_FsStaSignalMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,5,1,1,1),_FsStaSignalMacAddress_Type())
fsStaSignalMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaSignalMacAddress.setStatus(_A)
_FsStaSignalMacindex_Type=Unsigned32
_FsStaSignalMacindex_Object=MibTableColumn
fsStaSignalMacindex=_FsStaSignalMacindex_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,5,1,1,2),_FsStaSignalMacindex_Type())
fsStaSignalMacindex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaSignalMacindex.setStatus(_A)
_FsStaSignaltime_Type=DateAndTime
_FsStaSignaltime_Object=MibTableColumn
fsStaSignaltime=_FsStaSignaltime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,5,1,1,3),_FsStaSignaltime_Type())
fsStaSignaltime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaSignaltime.setStatus(_A)
_FsStaSignalValue_Type=Integer32
_FsStaSignalValue_Object=MibTableColumn
fsStaSignalValue=_FsStaSignalValue_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,5,1,1,4),_FsStaSignalValue_Type())
fsStaSignalValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaSignalValue.setStatus(_A)
_FsStaAssRetryByMAC_ObjectIdentity=ObjectIdentity
fsStaAssRetryByMAC=_FsStaAssRetryByMAC_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,6))
_FsStaAssRetryByMACTable_Object=MibTable
fsStaAssRetryByMACTable=_FsStaAssRetryByMACTable_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,6,1))
if mibBuilder.loadTexts:fsStaAssRetryByMACTable.setStatus(_A)
_FsStaAssRetryByMACEntry_Object=MibTableRow
fsStaAssRetryByMACEntry=_FsStaAssRetryByMACEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,6,1,1))
fsStaAssRetryByMACEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:fsStaAssRetryByMACEntry.setStatus(_A)
_FsStaRetryMacAddress_Type=MacAddress
_FsStaRetryMacAddress_Object=MibTableColumn
fsStaRetryMacAddress=_FsStaRetryMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,6,1,1,1),_FsStaRetryMacAddress_Type())
fsStaRetryMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaRetryMacAddress.setStatus(_A)
_FsStaRetryMacindex_Type=Unsigned32
_FsStaRetryMacindex_Object=MibTableColumn
fsStaRetryMacindex=_FsStaRetryMacindex_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,6,1,1,2),_FsStaRetryMacindex_Type())
fsStaRetryMacindex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsStaRetryMacindex.setStatus(_A)
_FsStaRetrytime_Type=DateAndTime
_FsStaRetrytime_Object=MibTableColumn
fsStaRetrytime=_FsStaRetrytime_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,6,1,1,3),_FsStaRetrytime_Type())
fsStaRetrytime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaRetrytime.setStatus(_A)
_FsStaRetryValue_Type=Integer32
_FsStaRetryValue_Object=MibTableColumn
fsStaRetryValue=_FsStaRetryValue_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,6,1,1,4),_FsStaRetryValue_Type())
fsStaRetryValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsStaRetryValue.setStatus(_A)
_FsStaAssStatistic_ObjectIdentity=ObjectIdentity
fsStaAssStatistic=_FsStaAssStatistic_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,1,7))
_FsAssStatisticsTotalsta_Type=Unsigned32
_FsAssStatisticsTotalsta_Object=MibScalar
fsAssStatisticsTotalsta=_FsAssStatisticsTotalsta_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,7,1),_FsAssStatisticsTotalsta_Type())
fsAssStatisticsTotalsta.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAssStatisticsTotalsta.setStatus(_A)
_FsAssStatisticsTotalinfo_Type=Unsigned32
_FsAssStatisticsTotalinfo_Object=MibScalar
fsAssStatisticsTotalinfo=_FsAssStatisticsTotalinfo_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,7,2),_FsAssStatisticsTotalinfo_Type())
fsAssStatisticsTotalinfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAssStatisticsTotalinfo.setStatus(_A)
_FsAssStatisticsdown_Type=Unsigned32
_FsAssStatisticsdown_Object=MibScalar
fsAssStatisticsdown=_FsAssStatisticsdown_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,7,3),_FsAssStatisticsdown_Type())
fsAssStatisticsdown.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAssStatisticsdown.setStatus(_A)
_FsAssStatisticsObligate1_Type=Unsigned32
_FsAssStatisticsObligate1_Object=MibScalar
fsAssStatisticsObligate1=_FsAssStatisticsObligate1_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,7,4),_FsAssStatisticsObligate1_Type())
fsAssStatisticsObligate1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAssStatisticsObligate1.setStatus(_A)
_FsAssStatisticsObligate2_Type=Unsigned32
_FsAssStatisticsObligate2_Object=MibScalar
fsAssStatisticsObligate2=_FsAssStatisticsObligate2_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,7,5),_FsAssStatisticsObligate2_Type())
fsAssStatisticsObligate2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAssStatisticsObligate2.setStatus(_A)
_FsAssStatisticsObligate3_Type=Unsigned32
_FsAssStatisticsObligate3_Object=MibScalar
fsAssStatisticsObligate3=_FsAssStatisticsObligate3_Object((1,3,6,1,4,1,52642,1,1,10,2,101,1,7,6),_FsAssStatisticsObligate3_Type())
fsAssStatisticsObligate3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAssStatisticsObligate3.setStatus(_A)
_FsStaAssRecordsMIBConformance_ObjectIdentity=ObjectIdentity
fsStaAssRecordsMIBConformance=_FsStaAssRecordsMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,2))
_FsStaAssRecordsMIBCompliances_ObjectIdentity=ObjectIdentity
fsStaAssRecordsMIBCompliances=_FsStaAssRecordsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,2,1))
_FsStaAssRecordsMIBGroups_ObjectIdentity=ObjectIdentity
fsStaAssRecordsMIBGroups=_FsStaAssRecordsMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,101,2,2))
fsStaAssRecordsGrobalMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,1))
fsStaAssRecordsGrobalMIBroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:fsStaAssRecordsGrobalMIBroup.setStatus(_A)
fsStaAssRecordsMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,2))
fsStaAssRecordsMIBroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:fsStaAssRecordsMIBroup.setStatus(_A)
fsStaAssRecordsSearchByTimeMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,3))
fsStaAssRecordsSearchByTimeMIBroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:fsStaAssRecordsSearchByTimeMIBroup.setStatus(_A)
fsStaAssRecordsSearchByAPMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,4))
fsStaAssRecordsSearchByAPMIBroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:fsStaAssRecordsSearchByAPMIBroup.setStatus(_A)
fsStaAssSignalSearchByMACMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,5))
fsStaAssSignalSearchByMACMIBroup.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:fsStaAssSignalSearchByMACMIBroup.setStatus(_A)
fsStaAssRetrySearchByMACMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,6))
fsStaAssRetrySearchByMACMIBroup.setObjects(*((_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:fsStaAssRetrySearchByMACMIBroup.setStatus(_A)
fsStaAssStatisticsMIBroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,101,2,2,7))
fsStaAssStatisticsMIBroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:fsStaAssStatisticsMIBroup.setStatus(_A)
fsStaAssRecordsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,101,2,1,1))
fsStaAssRecordsMIBCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:fsStaAssRecordsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsStaAssRecordsMIB':fsStaAssRecordsMIB,'fsStaAssRecordsMIBTrap':fsStaAssRecordsMIBTrap,'fsStaAssRecordsMIBObjects':fsStaAssRecordsMIBObjects,'fsStaAssRecordsGrobal':fsStaAssRecordsGrobal,'fsStaAssRecordsGrobalTable':fsStaAssRecordsGrobalTable,'fsStaAssRecordsGrobalEntry':fsStaAssRecordsGrobalEntry,_H:fsStaMacGrobalAddress,_V:fsStaMacGrobalAPName,_W:fsStaMacGrobalISUP,_X:fsStaMacGrobalStartime,_Y:fsStaMacGrobalupdowntimes,_Z:fsStaMacGrobalroamtimes,_a:fsStaMacGrobaltotaltimes,_b:fsStaMacGrobalrealdowntimes,_c:fsStaMacGrobalSSID,'fsStaAssRecordsByMAC':fsStaAssRecordsByMAC,'fsStaAssRecordsByMACTable':fsStaAssRecordsByMACTable,'fsStaAssRecordsByMACEntry':fsStaAssRecordsByMACEntry,_I:fsStaMacAddress,_J:fsStaMacindex,_d:fsStaAsstime,_e:fsStaAssAction,_f:fsStaAssSubAction,_g:fsStaAssResult,_h:fsStaAssReason,_i:fsStaAssApNamePre,_j:fsStaAssApNameNow,_k:fsStaAssSignalQua,_l:fsStaAssRoamtype,_m:fsStaAssjitter,_n:fsStaAssjointimes,_o:fsStaAsslatelytime,_p:fsStaAssSSID,'fsStaAssRecordsByTime':fsStaAssRecordsByTime,'fsStaAssRecordsSearchByTimeTable':fsStaAssRecordsSearchByTimeTable,'fsStaAssRecordsSearchByTimeEntry':fsStaAssRecordsSearchByTimeEntry,_K:fsStaUptimeLow,_L:fsStaUptimeHigh,_M:fsStaDowntimeLow,_N:fsStaDowntimeHigh,_O:fsStaTimeindex,_q:fsStaTimeMac,_r:fsStaTimeAPName,_s:fsStaTimeISUP,_t:fsStaTimeStartime,_u:fsStaTimeupdowntimes,_v:fsStaTimeroamtimes,_w:fsStaTimertotaltimes,_x:fsStaTimerjitter,_y:fsStaTimerjointimes,_z:fsStaTimerlatelytime,_A0:fsStaTimerSSID,'fsStaAssRecordsByAP':fsStaAssRecordsByAP,'fsStaAssRecordsSearchByAPTable':fsStaAssRecordsSearchByAPTable,'fsStaAssRecordsSearchByAPEntry':fsStaAssRecordsSearchByAPEntry,_P:fsStaAPAPName,_Q:fsStaAPindex,_A1:fsStaAPMac,_A2:fsStaAPISUP,_A3:fsStaAPStartime,_A4:fsStaAPupdowntimes,_A5:fsStaAProamtimes,_A6:fsStaAPtotaltimes,_A7:fsStaAPjitter,_A8:fsStaAPjointimes,_A9:fsStaAPlatelytime,_AA:fsStaAPSSID,'fsStaAssSignalByMAC':fsStaAssSignalByMAC,'fsStaAssSignalByMACTable':fsStaAssSignalByMACTable,'fsStaAssSignalByMACEntry':fsStaAssSignalByMACEntry,_R:fsStaSignalMacAddress,_S:fsStaSignalMacindex,_AB:fsStaSignaltime,_AC:fsStaSignalValue,'fsStaAssRetryByMAC':fsStaAssRetryByMAC,'fsStaAssRetryByMACTable':fsStaAssRetryByMACTable,'fsStaAssRetryByMACEntry':fsStaAssRetryByMACEntry,_T:fsStaRetryMacAddress,_U:fsStaRetryMacindex,_AD:fsStaRetrytime,_AE:fsStaRetryValue,'fsStaAssStatistic':fsStaAssStatistic,_AF:fsAssStatisticsTotalsta,_AG:fsAssStatisticsTotalinfo,_AH:fsAssStatisticsdown,_AI:fsAssStatisticsObligate1,_AJ:fsAssStatisticsObligate2,_AK:fsAssStatisticsObligate3,'fsStaAssRecordsMIBConformance':fsStaAssRecordsMIBConformance,'fsStaAssRecordsMIBCompliances':fsStaAssRecordsMIBCompliances,'fsStaAssRecordsMIBCompliance':fsStaAssRecordsMIBCompliance,'fsStaAssRecordsMIBGroups':fsStaAssRecordsMIBGroups,_AL:fsStaAssRecordsGrobalMIBroup,_AM:fsStaAssRecordsMIBroup,_AN:fsStaAssRecordsSearchByTimeMIBroup,_AO:fsStaAssRecordsSearchByAPMIBroup,_AP:fsStaAssSignalSearchByMACMIBroup,_AQ:fsStaAssRetrySearchByMACMIBroup,_AR:fsStaAssStatisticsMIBroup})