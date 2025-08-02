_P='ntcMpeEncConfGrpV1Standard'
_O='ntcMpeChanMacAddr'
_N='ntcMpeChanEnable'
_M='ntcMpeChanName'
_L='ntcMpeEncSignPmtPid'
_K='ntcMpeEncSignProgramNumber'
_J='ntcMpeEncSignEnable'
_I='ntcMpeEncDataPid'
_H='ntcMpeEncEnable'
_G='ntcMpeEncChannelsInx'
_F='DisplayString'
_E='Unsigned32'
_D='NtcEnable'
_C='read-write'
_B='NEWTEC-MPEENCAPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
ntcMpeEncaps=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1900))
if mibBuilder.loadTexts:ntcMpeEncaps.setRevisions(('2017-07-10 12:00','2013-03-27 10:00','2012-06-28 12:00'))
_NtcMpeEncObjects_ObjectIdentity=ObjectIdentity
ntcMpeEncObjects=_NtcMpeEncObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1900,1))
if mibBuilder.loadTexts:ntcMpeEncObjects.setStatus(_A)
class _NtcMpeEncEnable_Type(NtcEnable):defaultValue=0
_NtcMpeEncEnable_Type.__name__=_D
_NtcMpeEncEnable_Object=MibScalar
ntcMpeEncEnable=_NtcMpeEncEnable_Object((1,3,6,1,4,1,5835,5,2,1900,1,1),_NtcMpeEncEnable_Type())
ntcMpeEncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeEncEnable.setStatus(_A)
class _NtcMpeEncDataPid_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,8190))
_NtcMpeEncDataPid_Type.__name__=_E
_NtcMpeEncDataPid_Object=MibScalar
ntcMpeEncDataPid=_NtcMpeEncDataPid_Object((1,3,6,1,4,1,5835,5,2,1900,1,2),_NtcMpeEncDataPid_Type())
ntcMpeEncDataPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeEncDataPid.setStatus(_A)
class _NtcMpeEncSignEnable_Type(NtcEnable):defaultValue=0
_NtcMpeEncSignEnable_Type.__name__=_D
_NtcMpeEncSignEnable_Object=MibScalar
ntcMpeEncSignEnable=_NtcMpeEncSignEnable_Object((1,3,6,1,4,1,5835,5,2,1900,1,3),_NtcMpeEncSignEnable_Type())
ntcMpeEncSignEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeEncSignEnable.setStatus(_A)
class _NtcMpeEncSignProgramNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtcMpeEncSignProgramNumber_Type.__name__=_E
_NtcMpeEncSignProgramNumber_Object=MibScalar
ntcMpeEncSignProgramNumber=_NtcMpeEncSignProgramNumber_Object((1,3,6,1,4,1,5835,5,2,1900,1,4),_NtcMpeEncSignProgramNumber_Type())
ntcMpeEncSignProgramNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeEncSignProgramNumber.setStatus(_A)
class _NtcMpeEncSignPmtPid_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,8190))
_NtcMpeEncSignPmtPid_Type.__name__=_E
_NtcMpeEncSignPmtPid_Object=MibScalar
ntcMpeEncSignPmtPid=_NtcMpeEncSignPmtPid_Object((1,3,6,1,4,1,5835,5,2,1900,1,5),_NtcMpeEncSignPmtPid_Type())
ntcMpeEncSignPmtPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeEncSignPmtPid.setStatus(_A)
_NtcMpeEncChannelsTable_Object=MibTable
ntcMpeEncChannelsTable=_NtcMpeEncChannelsTable_Object((1,3,6,1,4,1,5835,5,2,1900,1,6))
if mibBuilder.loadTexts:ntcMpeEncChannelsTable.setStatus(_A)
_NtcMpeEncChannelsEntry_Object=MibTableRow
ntcMpeEncChannelsEntry=_NtcMpeEncChannelsEntry_Object((1,3,6,1,4,1,5835,5,2,1900,1,6,1))
ntcMpeEncChannelsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ntcMpeEncChannelsEntry.setStatus(_A)
_NtcMpeEncChannelsInx_Type=Unsigned32
_NtcMpeEncChannelsInx_Object=MibTableColumn
ntcMpeEncChannelsInx=_NtcMpeEncChannelsInx_Object((1,3,6,1,4,1,5835,5,2,1900,1,6,1,1),_NtcMpeEncChannelsInx_Type())
ntcMpeEncChannelsInx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntcMpeEncChannelsInx.setStatus(_A)
class _NtcMpeChanName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcMpeChanName_Type.__name__=_F
_NtcMpeChanName_Object=MibTableColumn
ntcMpeChanName=_NtcMpeChanName_Object((1,3,6,1,4,1,5835,5,2,1900,1,6,1,2),_NtcMpeChanName_Type())
ntcMpeChanName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeChanName.setStatus(_A)
class _NtcMpeChanEnable_Type(NtcEnable):defaultValue=0
_NtcMpeChanEnable_Type.__name__=_D
_NtcMpeChanEnable_Object=MibTableColumn
ntcMpeChanEnable=_NtcMpeChanEnable_Object((1,3,6,1,4,1,5835,5,2,1900,1,6,1,3),_NtcMpeChanEnable_Type())
ntcMpeChanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeChanEnable.setStatus(_A)
_NtcMpeChanMacAddr_Type=MacAddress
_NtcMpeChanMacAddr_Object=MibTableColumn
ntcMpeChanMacAddr=_NtcMpeChanMacAddr_Object((1,3,6,1,4,1,5835,5,2,1900,1,6,1,4),_NtcMpeChanMacAddr_Type())
ntcMpeChanMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMpeChanMacAddr.setStatus(_A)
_NtcMpeEncConformance_ObjectIdentity=ObjectIdentity
ntcMpeEncConformance=_NtcMpeEncConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1900,2))
if mibBuilder.loadTexts:ntcMpeEncConformance.setStatus(_A)
_NtcMpeEncConfCompliance_ObjectIdentity=ObjectIdentity
ntcMpeEncConfCompliance=_NtcMpeEncConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1900,2,1))
if mibBuilder.loadTexts:ntcMpeEncConfCompliance.setStatus(_A)
_NtcMpeEncConfGroup_ObjectIdentity=ObjectIdentity
ntcMpeEncConfGroup=_NtcMpeEncConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1900,2,2))
if mibBuilder.loadTexts:ntcMpeEncConfGroup.setStatus(_A)
ntcMpeEncConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1900,2,2,1))
ntcMpeEncConfGrpV1Standard.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ntcMpeEncConfGrpV1Standard.setStatus(_A)
ntcMpeEncConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1900,2,1,1))
ntcMpeEncConfCompV1Standard.setObjects((_B,_P))
if mibBuilder.loadTexts:ntcMpeEncConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcMpeEncaps':ntcMpeEncaps,'ntcMpeEncObjects':ntcMpeEncObjects,_H:ntcMpeEncEnable,_I:ntcMpeEncDataPid,_J:ntcMpeEncSignEnable,_K:ntcMpeEncSignProgramNumber,_L:ntcMpeEncSignPmtPid,'ntcMpeEncChannelsTable':ntcMpeEncChannelsTable,'ntcMpeEncChannelsEntry':ntcMpeEncChannelsEntry,_G:ntcMpeEncChannelsInx,_M:ntcMpeChanName,_N:ntcMpeChanEnable,_O:ntcMpeChanMacAddr,'ntcMpeEncConformance':ntcMpeEncConformance,'ntcMpeEncConfCompliance':ntcMpeEncConfCompliance,'ntcMpeEncConfCompV1Standard':ntcMpeEncConfCompV1Standard,'ntcMpeEncConfGroup':ntcMpeEncConfGroup,_P:ntcMpeEncConfGrpV1Standard})