_G='cienaWsPtpPluggableGroup'
_F='cwsPtpPluggableTxStatusLossOfLock'
_E='cwsPtpPluggableTxStatusLossOfSignal'
_D='cwsPtpAugPtpPluggableTxStatusEntry'
_C='read-only'
_B='CIENA-WS-PTP-PLUGGABLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
cwsPtpTxStatusEntry,=mibBuilder.importSymbols('CIENA-WS-PTP-MIB','cwsPtpTxStatusEntry')
ChannelsNumber,PtpId=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','ChannelsNumber','PtpId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsPtpPluggableMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,10))
if mibBuilder.loadTexts:cienaWsPtpPluggableMIB.setRevisions(('2017-02-28 00:00','2016-12-12 00:00','2016-06-14 00:00','2015-04-29 00:00'))
_CienaWsPtpPluggableObjects_ObjectIdentity=ObjectIdentity
cienaWsPtpPluggableObjects=_CienaWsPtpPluggableObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,10,1))
_CienaWsPtpPluggableConformance_ObjectIdentity=ObjectIdentity
cienaWsPtpPluggableConformance=_CienaWsPtpPluggableConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,10,2))
_CienaWsPtpPluggableGroups_ObjectIdentity=ObjectIdentity
cienaWsPtpPluggableGroups=_CienaWsPtpPluggableGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,10,2,1))
_CienaWsPtpPluggableCompliances_ObjectIdentity=ObjectIdentity
cienaWsPtpPluggableCompliances=_CienaWsPtpPluggableCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,10,2,2))
_CwsPtpAugPtpPluggableTxStatusTable_Object=MibTable
cwsPtpAugPtpPluggableTxStatusTable=_CwsPtpAugPtpPluggableTxStatusTable_Object((1,3,6,1,4,1,1271,3,4,10,3))
if mibBuilder.loadTexts:cwsPtpAugPtpPluggableTxStatusTable.setStatus(_A)
_CwsPtpAugPtpPluggableTxStatusEntry_Object=MibTableRow
cwsPtpAugPtpPluggableTxStatusEntry=_CwsPtpAugPtpPluggableTxStatusEntry_Object((1,3,6,1,4,1,1271,3,4,10,3,1))
if mibBuilder.loadTexts:cwsPtpAugPtpPluggableTxStatusEntry.setStatus(_A)
_CwsPtpPluggableTxStatusLossOfSignal_Type=TruthValue
_CwsPtpPluggableTxStatusLossOfSignal_Object=MibTableColumn
cwsPtpPluggableTxStatusLossOfSignal=_CwsPtpPluggableTxStatusLossOfSignal_Object((1,3,6,1,4,1,1271,3,4,10,3,1,1),_CwsPtpPluggableTxStatusLossOfSignal_Type())
cwsPtpPluggableTxStatusLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPluggableTxStatusLossOfSignal.setStatus(_A)
_CwsPtpPluggableTxStatusLossOfLock_Type=TruthValue
_CwsPtpPluggableTxStatusLossOfLock_Object=MibTableColumn
cwsPtpPluggableTxStatusLossOfLock=_CwsPtpPluggableTxStatusLossOfLock_Object((1,3,6,1,4,1,1271,3,4,10,3,1,2),_CwsPtpPluggableTxStatusLossOfLock_Type())
cwsPtpPluggableTxStatusLossOfLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPluggableTxStatusLossOfLock.setStatus(_A)
cwsPtpTxStatusEntry.registerAugmentions((_B,_D))
cwsPtpAugPtpPluggableTxStatusEntry.setIndexNames(*cwsPtpTxStatusEntry.getIndexNames())
cienaWsPtpPluggableGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,10,2,1,1))
cienaWsPtpPluggableGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:cienaWsPtpPluggableGroup.setStatus(_A)
cienaWsPtpPluggableCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,10,2,2,1))
cienaWsPtpPluggableCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:cienaWsPtpPluggableCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cienaWsPtpPluggableMIB':cienaWsPtpPluggableMIB,'cienaWsPtpPluggableObjects':cienaWsPtpPluggableObjects,'cienaWsPtpPluggableConformance':cienaWsPtpPluggableConformance,'cienaWsPtpPluggableGroups':cienaWsPtpPluggableGroups,_G:cienaWsPtpPluggableGroup,'cienaWsPtpPluggableCompliances':cienaWsPtpPluggableCompliances,'cienaWsPtpPluggableCompliance':cienaWsPtpPluggableCompliance,'cwsPtpAugPtpPluggableTxStatusTable':cwsPtpAugPtpPluggableTxStatusTable,_D:cwsPtpAugPtpPluggableTxStatusEntry,_E:cwsPtpPluggableTxStatusLossOfSignal,_F:cwsPtpPluggableTxStatusLossOfLock})