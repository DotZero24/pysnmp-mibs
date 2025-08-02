_F='carpGroupIndex'
_E='carpIfIndex'
_D='OPENBSD-CARP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
openBSD,=mibBuilder.importSymbols('OPENBSD-BASE-MIB','openBSD')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
carpMIBObjects=ModuleIdentity((1,3,6,1,4,1,30155,6))
if mibBuilder.loadTexts:carpMIBObjects.setRevisions(('2018-05-14 00:00','2012-01-31 00:00'))
_CarpSysctl_ObjectIdentity=ObjectIdentity
carpSysctl=_CarpSysctl_ObjectIdentity((1,3,6,1,4,1,30155,6,1))
_CarpAllow_Type=TruthValue
_CarpAllow_Object=MibScalar
carpAllow=_CarpAllow_Object((1,3,6,1,4,1,30155,6,1,1),_CarpAllow_Type())
carpAllow.setMaxAccess(_B)
if mibBuilder.loadTexts:carpAllow.setStatus(_A)
_CarpPreempt_Type=TruthValue
_CarpPreempt_Object=MibScalar
carpPreempt=_CarpPreempt_Object((1,3,6,1,4,1,30155,6,1,2),_CarpPreempt_Type())
carpPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPreempt.setStatus(_A)
_CarpLog_Type=TruthValue
_CarpLog_Object=MibScalar
carpLog=_CarpLog_Object((1,3,6,1,4,1,30155,6,1,3),_CarpLog_Type())
carpLog.setMaxAccess(_B)
if mibBuilder.loadTexts:carpLog.setStatus(_A)
_CarpIf_ObjectIdentity=ObjectIdentity
carpIf=_CarpIf_ObjectIdentity((1,3,6,1,4,1,30155,6,2))
_CarpIfNumber_Type=Integer32
_CarpIfNumber_Object=MibScalar
carpIfNumber=_CarpIfNumber_Object((1,3,6,1,4,1,30155,6,2,1),_CarpIfNumber_Type())
carpIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfNumber.setStatus(_A)
_CarpIfTable_Object=MibTable
carpIfTable=_CarpIfTable_Object((1,3,6,1,4,1,30155,6,2,2))
if mibBuilder.loadTexts:carpIfTable.setStatus(_A)
_CarpIfEntry_Object=MibTableRow
carpIfEntry=_CarpIfEntry_Object((1,3,6,1,4,1,30155,6,2,2,1))
carpIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:carpIfEntry.setStatus(_A)
class _CarpIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CarpIfIndex_Type.__name__=_C
_CarpIfIndex_Object=MibTableColumn
carpIfIndex=_CarpIfIndex_Object((1,3,6,1,4,1,30155,6,2,2,1,1),_CarpIfIndex_Type())
carpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfIndex.setStatus(_A)
_CarpIfDescr_Type=OctetString
_CarpIfDescr_Object=MibTableColumn
carpIfDescr=_CarpIfDescr_Object((1,3,6,1,4,1,30155,6,2,2,1,2),_CarpIfDescr_Type())
carpIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfDescr.setStatus(_A)
_CarpIfVhid_Type=Integer32
_CarpIfVhid_Object=MibTableColumn
carpIfVhid=_CarpIfVhid_Object((1,3,6,1,4,1,30155,6,2,2,1,3),_CarpIfVhid_Type())
carpIfVhid.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfVhid.setStatus(_A)
_CarpIfDev_Type=OctetString
_CarpIfDev_Object=MibTableColumn
carpIfDev=_CarpIfDev_Object((1,3,6,1,4,1,30155,6,2,2,1,4),_CarpIfDev_Type())
carpIfDev.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfDev.setStatus(_A)
_CarpIfAdvbase_Type=Integer32
_CarpIfAdvbase_Object=MibTableColumn
carpIfAdvbase=_CarpIfAdvbase_Object((1,3,6,1,4,1,30155,6,2,2,1,5),_CarpIfAdvbase_Type())
carpIfAdvbase.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfAdvbase.setStatus(_A)
_CarpIfAdvskew_Type=Integer32
_CarpIfAdvskew_Object=MibTableColumn
carpIfAdvskew=_CarpIfAdvskew_Object((1,3,6,1,4,1,30155,6,2,2,1,6),_CarpIfAdvskew_Type())
carpIfAdvskew.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfAdvskew.setStatus(_A)
class _CarpIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('init',0),('backup',1),('master',2)))
_CarpIfState_Type.__name__=_C
_CarpIfState_Object=MibTableColumn
carpIfState=_CarpIfState_Object((1,3,6,1,4,1,30155,6,2,2,1,7),_CarpIfState_Type())
carpIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIfState.setStatus(_A)
_CarpStats_ObjectIdentity=ObjectIdentity
carpStats=_CarpStats_ObjectIdentity((1,3,6,1,4,1,30155,6,3))
_CarpIpPktsRecv_Type=Counter64
_CarpIpPktsRecv_Object=MibScalar
carpIpPktsRecv=_CarpIpPktsRecv_Object((1,3,6,1,4,1,30155,6,3,1),_CarpIpPktsRecv_Type())
carpIpPktsRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIpPktsRecv.setStatus(_A)
_CarpIp6PktsRecv_Type=Counter64
_CarpIp6PktsRecv_Object=MibScalar
carpIp6PktsRecv=_CarpIp6PktsRecv_Object((1,3,6,1,4,1,30155,6,3,2),_CarpIp6PktsRecv_Type())
carpIp6PktsRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIp6PktsRecv.setStatus(_A)
_CarpPktDiscardsForBadInterface_Type=Counter64
_CarpPktDiscardsForBadInterface_Object=MibScalar
carpPktDiscardsForBadInterface=_CarpPktDiscardsForBadInterface_Object((1,3,6,1,4,1,30155,6,3,3),_CarpPktDiscardsForBadInterface_Type())
carpPktDiscardsForBadInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForBadInterface.setStatus(_A)
_CarpPktDiscardsForWrongTtl_Type=Counter64
_CarpPktDiscardsForWrongTtl_Object=MibScalar
carpPktDiscardsForWrongTtl=_CarpPktDiscardsForWrongTtl_Object((1,3,6,1,4,1,30155,6,3,4),_CarpPktDiscardsForWrongTtl_Type())
carpPktDiscardsForWrongTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForWrongTtl.setStatus(_A)
_CarpPktShorterThanHeader_Type=Counter64
_CarpPktShorterThanHeader_Object=MibScalar
carpPktShorterThanHeader=_CarpPktShorterThanHeader_Object((1,3,6,1,4,1,30155,6,3,5),_CarpPktShorterThanHeader_Type())
carpPktShorterThanHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktShorterThanHeader.setStatus(_A)
_CarpPktDiscardsForBadChecksum_Type=Counter64
_CarpPktDiscardsForBadChecksum_Object=MibScalar
carpPktDiscardsForBadChecksum=_CarpPktDiscardsForBadChecksum_Object((1,3,6,1,4,1,30155,6,3,6),_CarpPktDiscardsForBadChecksum_Type())
carpPktDiscardsForBadChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForBadChecksum.setStatus(_A)
_CarpPktDiscardsForBadVersion_Type=Counter64
_CarpPktDiscardsForBadVersion_Object=MibScalar
carpPktDiscardsForBadVersion=_CarpPktDiscardsForBadVersion_Object((1,3,6,1,4,1,30155,6,3,7),_CarpPktDiscardsForBadVersion_Type())
carpPktDiscardsForBadVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForBadVersion.setStatus(_A)
_CarpPktDiscardsForTooShort_Type=Counter64
_CarpPktDiscardsForTooShort_Object=MibScalar
carpPktDiscardsForTooShort=_CarpPktDiscardsForTooShort_Object((1,3,6,1,4,1,30155,6,3,8),_CarpPktDiscardsForTooShort_Type())
carpPktDiscardsForTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForTooShort.setStatus(_A)
_CarpPktDiscardsForBadAuth_Type=Counter64
_CarpPktDiscardsForBadAuth_Object=MibScalar
carpPktDiscardsForBadAuth=_CarpPktDiscardsForBadAuth_Object((1,3,6,1,4,1,30155,6,3,9),_CarpPktDiscardsForBadAuth_Type())
carpPktDiscardsForBadAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForBadAuth.setStatus(_A)
_CarpPktDiscardsForBadVhid_Type=Counter64
_CarpPktDiscardsForBadVhid_Object=MibScalar
carpPktDiscardsForBadVhid=_CarpPktDiscardsForBadVhid_Object((1,3,6,1,4,1,30155,6,3,10),_CarpPktDiscardsForBadVhid_Type())
carpPktDiscardsForBadVhid.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForBadVhid.setStatus(_A)
_CarpPktDiscardsForBadAddressList_Type=Counter64
_CarpPktDiscardsForBadAddressList_Object=MibScalar
carpPktDiscardsForBadAddressList=_CarpPktDiscardsForBadAddressList_Object((1,3,6,1,4,1,30155,6,3,11),_CarpPktDiscardsForBadAddressList_Type())
carpPktDiscardsForBadAddressList.setMaxAccess(_B)
if mibBuilder.loadTexts:carpPktDiscardsForBadAddressList.setStatus(_A)
_CarpIpPktsSent_Type=Counter64
_CarpIpPktsSent_Object=MibScalar
carpIpPktsSent=_CarpIpPktsSent_Object((1,3,6,1,4,1,30155,6,3,12),_CarpIpPktsSent_Type())
carpIpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIpPktsSent.setStatus(_A)
_CarpIp6PktsSent_Type=Counter64
_CarpIp6PktsSent_Object=MibScalar
carpIp6PktsSent=_CarpIp6PktsSent_Object((1,3,6,1,4,1,30155,6,3,13),_CarpIp6PktsSent_Type())
carpIp6PktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:carpIp6PktsSent.setStatus(_A)
_CarpNoMemory_Type=Counter64
_CarpNoMemory_Object=MibScalar
carpNoMemory=_CarpNoMemory_Object((1,3,6,1,4,1,30155,6,3,14),_CarpNoMemory_Type())
carpNoMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:carpNoMemory.setStatus(_A)
_CarpTransitionsToMaster_Type=Counter64
_CarpTransitionsToMaster_Object=MibScalar
carpTransitionsToMaster=_CarpTransitionsToMaster_Object((1,3,6,1,4,1,30155,6,3,15),_CarpTransitionsToMaster_Type())
carpTransitionsToMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:carpTransitionsToMaster.setStatus(_A)
_CarpGroupTable_Object=MibTable
carpGroupTable=_CarpGroupTable_Object((1,3,6,1,4,1,30155,6,4))
if mibBuilder.loadTexts:carpGroupTable.setStatus(_A)
_CarpGroupEntry_Object=MibTableRow
carpGroupEntry=_CarpGroupEntry_Object((1,3,6,1,4,1,30155,6,4,1))
carpGroupEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:carpGroupEntry.setStatus(_A)
class _CarpGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CarpGroupIndex_Type.__name__=_C
_CarpGroupIndex_Object=MibTableColumn
carpGroupIndex=_CarpGroupIndex_Object((1,3,6,1,4,1,30155,6,4,1,1),_CarpGroupIndex_Type())
carpGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:carpGroupIndex.setStatus(_A)
_CarpGroupName_Type=OctetString
_CarpGroupName_Object=MibTableColumn
carpGroupName=_CarpGroupName_Object((1,3,6,1,4,1,30155,6,4,1,2),_CarpGroupName_Type())
carpGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:carpGroupName.setStatus(_A)
class _CarpGroupDemote_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CarpGroupDemote_Type.__name__=_C
_CarpGroupDemote_Object=MibTableColumn
carpGroupDemote=_CarpGroupDemote_Object((1,3,6,1,4,1,30155,6,4,1,3),_CarpGroupDemote_Type())
carpGroupDemote.setMaxAccess(_B)
if mibBuilder.loadTexts:carpGroupDemote.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'carpMIBObjects':carpMIBObjects,'carpSysctl':carpSysctl,'carpAllow':carpAllow,'carpPreempt':carpPreempt,'carpLog':carpLog,'carpIf':carpIf,'carpIfNumber':carpIfNumber,'carpIfTable':carpIfTable,'carpIfEntry':carpIfEntry,_E:carpIfIndex,'carpIfDescr':carpIfDescr,'carpIfVhid':carpIfVhid,'carpIfDev':carpIfDev,'carpIfAdvbase':carpIfAdvbase,'carpIfAdvskew':carpIfAdvskew,'carpIfState':carpIfState,'carpStats':carpStats,'carpIpPktsRecv':carpIpPktsRecv,'carpIp6PktsRecv':carpIp6PktsRecv,'carpPktDiscardsForBadInterface':carpPktDiscardsForBadInterface,'carpPktDiscardsForWrongTtl':carpPktDiscardsForWrongTtl,'carpPktShorterThanHeader':carpPktShorterThanHeader,'carpPktDiscardsForBadChecksum':carpPktDiscardsForBadChecksum,'carpPktDiscardsForBadVersion':carpPktDiscardsForBadVersion,'carpPktDiscardsForTooShort':carpPktDiscardsForTooShort,'carpPktDiscardsForBadAuth':carpPktDiscardsForBadAuth,'carpPktDiscardsForBadVhid':carpPktDiscardsForBadVhid,'carpPktDiscardsForBadAddressList':carpPktDiscardsForBadAddressList,'carpIpPktsSent':carpIpPktsSent,'carpIp6PktsSent':carpIp6PktsSent,'carpNoMemory':carpNoMemory,'carpTransitionsToMaster':carpTransitionsToMaster,'carpGroupTable':carpGroupTable,'carpGroupEntry':carpGroupEntry,_F:carpGroupIndex,'carpGroupName':carpGroupName,'carpGroupDemote':carpGroupDemote})