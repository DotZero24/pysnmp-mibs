_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TestAndIncr')
_Hirschmann_ObjectIdentity=ObjectIdentity
hirschmann=_Hirschmann_ObjectIdentity((1,3,6,1,4,1,248))
_HmMgmtSEEErrorIDGroup_ObjectIdentity=ObjectIdentity
hmMgmtSEEErrorIDGroup=_HmMgmtSEEErrorIDGroup_ObjectIdentity((1,3,6,1,4,1,248,16,2))
_HmRedundancyConflict_ObjectIdentity=ObjectIdentity
hmRedundancyConflict=_HmRedundancyConflict_ObjectIdentity((1,3,6,1,4,1,248,16,2,1))
if mibBuilder.loadTexts:hmRedundancyConflict.setStatus(_A)
_HmRedundancyConflictPort_ObjectIdentity=ObjectIdentity
hmRedundancyConflictPort=_HmRedundancyConflictPort_ObjectIdentity((1,3,6,1,4,1,248,16,2,2))
if mibBuilder.loadTexts:hmRedundancyConflictPort.setStatus(_A)
_HmMaxNumExceeded_ObjectIdentity=ObjectIdentity
hmMaxNumExceeded=_HmMaxNumExceeded_ObjectIdentity((1,3,6,1,4,1,248,16,2,3))
if mibBuilder.loadTexts:hmMaxNumExceeded.setStatus(_A)
_HmAlreadyCreated_ObjectIdentity=ObjectIdentity
hmAlreadyCreated=_HmAlreadyCreated_ObjectIdentity((1,3,6,1,4,1,248,16,2,4))
if mibBuilder.loadTexts:hmAlreadyCreated.setStatus(_A)
_HmRedundancyConflictFpgaPort_ObjectIdentity=ObjectIdentity
hmRedundancyConflictFpgaPort=_HmRedundancyConflictFpgaPort_ObjectIdentity((1,3,6,1,4,1,248,16,2,5))
if mibBuilder.loadTexts:hmRedundancyConflictFpgaPort.setStatus(_A)
_HmGenericEnableConflict_ObjectIdentity=ObjectIdentity
hmGenericEnableConflict=_HmGenericEnableConflict_ObjectIdentity((1,3,6,1,4,1,248,16,2,6))
if mibBuilder.loadTexts:hmGenericEnableConflict.setStatus(_A)
_HmRedundancyConflictPortShort_ObjectIdentity=ObjectIdentity
hmRedundancyConflictPortShort=_HmRedundancyConflictPortShort_ObjectIdentity((1,3,6,1,4,1,248,16,2,7))
if mibBuilder.loadTexts:hmRedundancyConflictPortShort.setStatus(_A)
_HmTableFullError_ObjectIdentity=ObjectIdentity
hmTableFullError=_HmTableFullError_ObjectIdentity((1,3,6,1,4,1,248,16,2,8))
if mibBuilder.loadTexts:hmTableFullError.setStatus(_A)
_HmFunctionNotUsableWithInterface_ObjectIdentity=ObjectIdentity
hmFunctionNotUsableWithInterface=_HmFunctionNotUsableWithInterface_ObjectIdentity((1,3,6,1,4,1,248,16,2,9))
if mibBuilder.loadTexts:hmFunctionNotUsableWithInterface.setStatus(_A)
_HmGeneralConflict_ObjectIdentity=ObjectIdentity
hmGeneralConflict=_HmGeneralConflict_ObjectIdentity((1,3,6,1,4,1,248,16,2,10))
if mibBuilder.loadTexts:hmGeneralConflict.setStatus(_A)
_HmGeneralExceededRange_ObjectIdentity=ObjectIdentity
hmGeneralExceededRange=_HmGeneralExceededRange_ObjectIdentity((1,3,6,1,4,1,248,16,2,11))
if mibBuilder.loadTexts:hmGeneralExceededRange.setStatus(_A)
_HmGenericDisableConflict_ObjectIdentity=ObjectIdentity
hmGenericDisableConflict=_HmGenericDisableConflict_ObjectIdentity((1,3,6,1,4,1,248,16,2,12))
if mibBuilder.loadTexts:hmGenericDisableConflict.setStatus(_A)
_HmRmonAlarmTableFullErrorReturn_ObjectIdentity=ObjectIdentity
hmRmonAlarmTableFullErrorReturn=_HmRmonAlarmTableFullErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,16,2,100))
if mibBuilder.loadTexts:hmRmonAlarmTableFullErrorReturn.setStatus(_A)
_HmMgmtUdpPortInUse_ObjectIdentity=ObjectIdentity
hmMgmtUdpPortInUse=_HmMgmtUdpPortInUse_ObjectIdentity((1,3,6,1,4,1,248,16,2,200))
if mibBuilder.loadTexts:hmMgmtUdpPortInUse.setStatus(_A)
_HmMgmtTcpPortInUse_ObjectIdentity=ObjectIdentity
hmMgmtTcpPortInUse=_HmMgmtTcpPortInUse_ObjectIdentity((1,3,6,1,4,1,248,16,2,201))
if mibBuilder.loadTexts:hmMgmtTcpPortInUse.setStatus(_A)
_HmMgmtIPAddressConflictWithMgmtIP_ObjectIdentity=ObjectIdentity
hmMgmtIPAddressConflictWithMgmtIP=_HmMgmtIPAddressConflictWithMgmtIP_ObjectIdentity((1,3,6,1,4,1,248,16,2,202))
if mibBuilder.loadTexts:hmMgmtIPAddressConflictWithMgmtIP.setStatus(_A)
_HmMgmtIPAddressConflictWithOobIP_ObjectIdentity=ObjectIdentity
hmMgmtIPAddressConflictWithOobIP=_HmMgmtIPAddressConflictWithOobIP_ObjectIdentity((1,3,6,1,4,1,248,16,2,203))
if mibBuilder.loadTexts:hmMgmtIPAddressConflictWithOobIP.setStatus(_A)
_HmMgmtIPAddressConflictWithRouterIP_ObjectIdentity=ObjectIdentity
hmMgmtIPAddressConflictWithRouterIP=_HmMgmtIPAddressConflictWithRouterIP_ObjectIdentity((1,3,6,1,4,1,248,16,2,204))
if mibBuilder.loadTexts:hmMgmtIPAddressConflictWithRouterIP.setStatus(_A)
_HmMgmtIPAddressConflictWithOobUsbIP_ObjectIdentity=ObjectIdentity
hmMgmtIPAddressConflictWithOobUsbIP=_HmMgmtIPAddressConflictWithOobUsbIP_ObjectIdentity((1,3,6,1,4,1,248,16,2,205))
if mibBuilder.loadTexts:hmMgmtIPAddressConflictWithOobUsbIP.setStatus(_A)
_Hm2NetIPAddrInvalid_ObjectIdentity=ObjectIdentity
hm2NetIPAddrInvalid=_Hm2NetIPAddrInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,300))
if mibBuilder.loadTexts:hm2NetIPAddrInvalid.setStatus(_A)
_Hm2NetIPAddrAndGateway_ObjectIdentity=ObjectIdentity
hm2NetIPAddrAndGateway=_Hm2NetIPAddrAndGateway_ObjectIdentity((1,3,6,1,4,1,248,16,2,301))
if mibBuilder.loadTexts:hm2NetIPAddrAndGateway.setStatus(_A)
_Hm2NetIPAddrAndSubnet_ObjectIdentity=ObjectIdentity
hm2NetIPAddrAndSubnet=_Hm2NetIPAddrAndSubnet_ObjectIdentity((1,3,6,1,4,1,248,16,2,302))
if mibBuilder.loadTexts:hm2NetIPAddrAndSubnet.setStatus(_A)
_Hm2NetPrefixLengthInvalid_ObjectIdentity=ObjectIdentity
hm2NetPrefixLengthInvalid=_Hm2NetPrefixLengthInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,303))
if mibBuilder.loadTexts:hm2NetPrefixLengthInvalid.setStatus(_A)
_Hm2VlanIdNotExists_ObjectIdentity=ObjectIdentity
hm2VlanIdNotExists=_Hm2VlanIdNotExists_ObjectIdentity((1,3,6,1,4,1,248,16,2,304))
if mibBuilder.loadTexts:hm2VlanIdNotExists.setStatus(_A)
_Hm2NetIPv6AddressAlreadyExists_ObjectIdentity=ObjectIdentity
hm2NetIPv6AddressAlreadyExists=_Hm2NetIPv6AddressAlreadyExists_ObjectIdentity((1,3,6,1,4,1,248,16,2,400))
if mibBuilder.loadTexts:hm2NetIPv6AddressAlreadyExists.setStatus(_A)
_Hm2NetIPv6ChangeEUIWhileEntryActive_ObjectIdentity=ObjectIdentity
hm2NetIPv6ChangeEUIWhileEntryActive=_Hm2NetIPv6ChangeEUIWhileEntryActive_ObjectIdentity((1,3,6,1,4,1,248,16,2,401))
if mibBuilder.loadTexts:hm2NetIPv6ChangeEUIWhileEntryActive.setStatus(_A)
_Hm2NetIPv6ChangeAddressWhileEntryActive_ObjectIdentity=ObjectIdentity
hm2NetIPv6ChangeAddressWhileEntryActive=_Hm2NetIPv6ChangeAddressWhileEntryActive_ObjectIdentity((1,3,6,1,4,1,248,16,2,402))
if mibBuilder.loadTexts:hm2NetIPv6ChangeAddressWhileEntryActive.setStatus(_A)
_Hm2NetIPv6IncorrectFamilyType_ObjectIdentity=ObjectIdentity
hm2NetIPv6IncorrectFamilyType=_Hm2NetIPv6IncorrectFamilyType_ObjectIdentity((1,3,6,1,4,1,248,16,2,403))
if mibBuilder.loadTexts:hm2NetIPv6IncorrectFamilyType.setStatus(_A)
_Hm2NetIPv6EnableEUIWhilePrefixLenNot64_ObjectIdentity=ObjectIdentity
hm2NetIPv6EnableEUIWhilePrefixLenNot64=_Hm2NetIPv6EnableEUIWhilePrefixLenNot64_ObjectIdentity((1,3,6,1,4,1,248,16,2,404))
if mibBuilder.loadTexts:hm2NetIPv6EnableEUIWhilePrefixLenNot64.setStatus(_A)
_Hm2NetIPv6ChangeAddressOrigin_ObjectIdentity=ObjectIdentity
hm2NetIPv6ChangeAddressOrigin=_Hm2NetIPv6ChangeAddressOrigin_ObjectIdentity((1,3,6,1,4,1,248,16,2,405))
if mibBuilder.loadTexts:hm2NetIPv6ChangeAddressOrigin.setStatus(_A)
_Hm2NetIPv6MaximumNumberStaticAddresses_ObjectIdentity=ObjectIdentity
hm2NetIPv6MaximumNumberStaticAddresses=_Hm2NetIPv6MaximumNumberStaticAddresses_ObjectIdentity((1,3,6,1,4,1,248,16,2,406))
if mibBuilder.loadTexts:hm2NetIPv6MaximumNumberStaticAddresses.setStatus(_A)
_Hm2NetIPv6IncorrectAddressLength_ObjectIdentity=ObjectIdentity
hm2NetIPv6IncorrectAddressLength=_Hm2NetIPv6IncorrectAddressLength_ObjectIdentity((1,3,6,1,4,1,248,16,2,407))
if mibBuilder.loadTexts:hm2NetIPv6IncorrectAddressLength.setStatus(_A)
_Hm2NetIPv6AddressPrefixNotMatching_ObjectIdentity=ObjectIdentity
hm2NetIPv6AddressPrefixNotMatching=_Hm2NetIPv6AddressPrefixNotMatching_ObjectIdentity((1,3,6,1,4,1,248,16,2,408))
if mibBuilder.loadTexts:hm2NetIPv6AddressPrefixNotMatching.setStatus(_A)
_Hm2NetIPv6PrefixNotSupported_ObjectIdentity=ObjectIdentity
hm2NetIPv6PrefixNotSupported=_Hm2NetIPv6PrefixNotSupported_ObjectIdentity((1,3,6,1,4,1,248,16,2,409))
if mibBuilder.loadTexts:hm2NetIPv6PrefixNotSupported.setStatus(_A)
_Hm2NetIPv6CannotAddReservedAddress_ObjectIdentity=ObjectIdentity
hm2NetIPv6CannotAddReservedAddress=_Hm2NetIPv6CannotAddReservedAddress_ObjectIdentity((1,3,6,1,4,1,248,16,2,410))
if mibBuilder.loadTexts:hm2NetIPv6CannotAddReservedAddress.setStatus(_A)
_Hm2EntryLenCharset_ObjectIdentity=ObjectIdentity
hm2EntryLenCharset=_Hm2EntryLenCharset_ObjectIdentity((1,3,6,1,4,1,248,16,2,411))
if mibBuilder.loadTexts:hm2EntryLenCharset.setStatus(_A)
_Hm2UserPwdLen_ObjectIdentity=ObjectIdentity
hm2UserPwdLen=_Hm2UserPwdLen_ObjectIdentity((1,3,6,1,4,1,248,16,2,412))
if mibBuilder.loadTexts:hm2UserPwdLen.setStatus(_A)
_Hm2EntryNotExist_ObjectIdentity=ObjectIdentity
hm2EntryNotExist=_Hm2EntryNotExist_ObjectIdentity((1,3,6,1,4,1,248,16,2,413))
if mibBuilder.loadTexts:hm2EntryNotExist.setStatus(_A)
_Hm2MaxNumUserExceeded_ObjectIdentity=ObjectIdentity
hm2MaxNumUserExceeded=_Hm2MaxNumUserExceeded_ObjectIdentity((1,3,6,1,4,1,248,16,2,414))
if mibBuilder.loadTexts:hm2MaxNumUserExceeded.setStatus(_A)
_Hm2NetIPv6UnreachableGatewaySubnet_ObjectIdentity=ObjectIdentity
hm2NetIPv6UnreachableGatewaySubnet=_Hm2NetIPv6UnreachableGatewaySubnet_ObjectIdentity((1,3,6,1,4,1,248,16,2,415))
if mibBuilder.loadTexts:hm2NetIPv6UnreachableGatewaySubnet.setStatus(_A)
_Hm2GenericDeleteError_ObjectIdentity=ObjectIdentity
hm2GenericDeleteError=_Hm2GenericDeleteError_ObjectIdentity((1,3,6,1,4,1,248,16,2,450))
if mibBuilder.loadTexts:hm2GenericDeleteError.setStatus(_A)
_Hm2GenericCreateError_ObjectIdentity=ObjectIdentity
hm2GenericCreateError=_Hm2GenericCreateError_ObjectIdentity((1,3,6,1,4,1,248,16,2,451))
if mibBuilder.loadTexts:hm2GenericCreateError.setStatus(_A)
_Hm2GenericEntryNotExist_ObjectIdentity=ObjectIdentity
hm2GenericEntryNotExist=_Hm2GenericEntryNotExist_ObjectIdentity((1,3,6,1,4,1,248,16,2,452))
if mibBuilder.loadTexts:hm2GenericEntryNotExist.setStatus(_A)
_Hm2GenericIPv4IPv6Supported_ObjectIdentity=ObjectIdentity
hm2GenericIPv4IPv6Supported=_Hm2GenericIPv4IPv6Supported_ObjectIdentity((1,3,6,1,4,1,248,16,2,453))
if mibBuilder.loadTexts:hm2GenericIPv4IPv6Supported.setStatus(_A)
_Hm2GenericMulticastAddrNotAllowed_ObjectIdentity=ObjectIdentity
hm2GenericMulticastAddrNotAllowed=_Hm2GenericMulticastAddrNotAllowed_ObjectIdentity((1,3,6,1,4,1,248,16,2,454))
if mibBuilder.loadTexts:hm2GenericMulticastAddrNotAllowed.setStatus(_A)
_Hm2GenericIPAddrInvalid_ObjectIdentity=ObjectIdentity
hm2GenericIPAddrInvalid=_Hm2GenericIPAddrInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,455))
if mibBuilder.loadTexts:hm2GenericIPAddrInvalid.setStatus(_A)
_Hm2GenericSourcePortInvalid_ObjectIdentity=ObjectIdentity
hm2GenericSourcePortInvalid=_Hm2GenericSourcePortInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,456))
if mibBuilder.loadTexts:hm2GenericSourcePortInvalid.setStatus(_A)
_Hm2GenericRowCommitError_ObjectIdentity=ObjectIdentity
hm2GenericRowCommitError=_Hm2GenericRowCommitError_ObjectIdentity((1,3,6,1,4,1,248,16,2,457))
if mibBuilder.loadTexts:hm2GenericRowCommitError.setStatus(_A)
_Hm2GenericDestIPAddrInvalid_ObjectIdentity=ObjectIdentity
hm2GenericDestIPAddrInvalid=_Hm2GenericDestIPAddrInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,458))
if mibBuilder.loadTexts:hm2GenericDestIPAddrInvalid.setStatus(_A)
_Hm2GenericDestMACAddrInvalid_ObjectIdentity=ObjectIdentity
hm2GenericDestMACAddrInvalid=_Hm2GenericDestMACAddrInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,459))
if mibBuilder.loadTexts:hm2GenericDestMACAddrInvalid.setStatus(_A)
_Hm2GenericDestPortInvalid_ObjectIdentity=ObjectIdentity
hm2GenericDestPortInvalid=_Hm2GenericDestPortInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,460))
if mibBuilder.loadTexts:hm2GenericDestPortInvalid.setStatus(_A)
_Hm2GenericSourceIPAddrInvalid_ObjectIdentity=ObjectIdentity
hm2GenericSourceIPAddrInvalid=_Hm2GenericSourceIPAddrInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,461))
if mibBuilder.loadTexts:hm2GenericSourceIPAddrInvalid.setStatus(_A)
_Hm2GenericSourceMACAddrInvalid_ObjectIdentity=ObjectIdentity
hm2GenericSourceMACAddrInvalid=_Hm2GenericSourceMACAddrInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,462))
if mibBuilder.loadTexts:hm2GenericSourceMACAddrInvalid.setStatus(_A)
_Hm2GenericEntryInvalid_ObjectIdentity=ObjectIdentity
hm2GenericEntryInvalid=_Hm2GenericEntryInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,463))
if mibBuilder.loadTexts:hm2GenericEntryInvalid.setStatus(_A)
_Hm2GenericInterfaceInvalid_ObjectIdentity=ObjectIdentity
hm2GenericInterfaceInvalid=_Hm2GenericInterfaceInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,464))
if mibBuilder.loadTexts:hm2GenericInterfaceInvalid.setStatus(_A)
_Hm2GenericOnlySupportsIPv4_ObjectIdentity=ObjectIdentity
hm2GenericOnlySupportsIPv4=_Hm2GenericOnlySupportsIPv4_ObjectIdentity((1,3,6,1,4,1,248,16,2,465))
if mibBuilder.loadTexts:hm2GenericOnlySupportsIPv4.setStatus(_A)
_Hm2GenericVlanIdInvalid_ObjectIdentity=ObjectIdentity
hm2GenericVlanIdInvalid=_Hm2GenericVlanIdInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,466))
if mibBuilder.loadTexts:hm2GenericVlanIdInvalid.setStatus(_A)
_Hm2GenericCommitInProgress_ObjectIdentity=ObjectIdentity
hm2GenericCommitInProgress=_Hm2GenericCommitInProgress_ObjectIdentity((1,3,6,1,4,1,248,16,2,467))
if mibBuilder.loadTexts:hm2GenericCommitInProgress.setStatus(_A)
_Hm2GenericNameInvalid_ObjectIdentity=ObjectIdentity
hm2GenericNameInvalid=_Hm2GenericNameInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,468))
if mibBuilder.loadTexts:hm2GenericNameInvalid.setStatus(_A)
_Hm2GenericDirectionInvalid_ObjectIdentity=ObjectIdentity
hm2GenericDirectionInvalid=_Hm2GenericDirectionInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,472))
if mibBuilder.loadTexts:hm2GenericDirectionInvalid.setStatus(_A)
_Hm2GenericNameAlreadyExist_ObjectIdentity=ObjectIdentity
hm2GenericNameAlreadyExist=_Hm2GenericNameAlreadyExist_ObjectIdentity((1,3,6,1,4,1,248,16,2,473))
if mibBuilder.loadTexts:hm2GenericNameAlreadyExist.setStatus(_A)
_Hm2GenericMinEntryInvalid_ObjectIdentity=ObjectIdentity
hm2GenericMinEntryInvalid=_Hm2GenericMinEntryInvalid_ObjectIdentity((1,3,6,1,4,1,248,16,2,474))
if mibBuilder.loadTexts:hm2GenericMinEntryInvalid.setStatus(_A)
_Hm2GenericEntryExistInSharedTable_ObjectIdentity=ObjectIdentity
hm2GenericEntryExistInSharedTable=_Hm2GenericEntryExistInSharedTable_ObjectIdentity((1,3,6,1,4,1,248,16,2,475))
if mibBuilder.loadTexts:hm2GenericEntryExistInSharedTable.setStatus(_A)
_Hm2GenericEntryIsReadOnly_ObjectIdentity=ObjectIdentity
hm2GenericEntryIsReadOnly=_Hm2GenericEntryIsReadOnly_ObjectIdentity((1,3,6,1,4,1,248,16,2,476))
if mibBuilder.loadTexts:hm2GenericEntryIsReadOnly.setStatus(_A)
_HmMgmtSEInfoIDGroup_ObjectIdentity=ObjectIdentity
hmMgmtSEInfoIDGroup=_HmMgmtSEInfoIDGroup_ObjectIdentity((1,3,6,1,4,1,248,16,3))
_HmMgmtSEInfoValueChanged_ObjectIdentity=ObjectIdentity
hmMgmtSEInfoValueChanged=_HmMgmtSEInfoValueChanged_ObjectIdentity((1,3,6,1,4,1,248,16,3,1))
if mibBuilder.loadTexts:hmMgmtSEInfoValueChanged.setStatus(_A)
mibBuilder.exportSymbols('HIRSCHMANN-GENERIC-ERROR-MIB',**{'hirschmann':hirschmann,'hmMgmtSEEErrorIDGroup':hmMgmtSEEErrorIDGroup,'hmRedundancyConflict':hmRedundancyConflict,'hmRedundancyConflictPort':hmRedundancyConflictPort,'hmMaxNumExceeded':hmMaxNumExceeded,'hmAlreadyCreated':hmAlreadyCreated,'hmRedundancyConflictFpgaPort':hmRedundancyConflictFpgaPort,'hmGenericEnableConflict':hmGenericEnableConflict,'hmRedundancyConflictPortShort':hmRedundancyConflictPortShort,'hmTableFullError':hmTableFullError,'hmFunctionNotUsableWithInterface':hmFunctionNotUsableWithInterface,'hmGeneralConflict':hmGeneralConflict,'hmGeneralExceededRange':hmGeneralExceededRange,'hmGenericDisableConflict':hmGenericDisableConflict,'hmRmonAlarmTableFullErrorReturn':hmRmonAlarmTableFullErrorReturn,'hmMgmtUdpPortInUse':hmMgmtUdpPortInUse,'hmMgmtTcpPortInUse':hmMgmtTcpPortInUse,'hmMgmtIPAddressConflictWithMgmtIP':hmMgmtIPAddressConflictWithMgmtIP,'hmMgmtIPAddressConflictWithOobIP':hmMgmtIPAddressConflictWithOobIP,'hmMgmtIPAddressConflictWithRouterIP':hmMgmtIPAddressConflictWithRouterIP,'hmMgmtIPAddressConflictWithOobUsbIP':hmMgmtIPAddressConflictWithOobUsbIP,'hm2NetIPAddrInvalid':hm2NetIPAddrInvalid,'hm2NetIPAddrAndGateway':hm2NetIPAddrAndGateway,'hm2NetIPAddrAndSubnet':hm2NetIPAddrAndSubnet,'hm2NetPrefixLengthInvalid':hm2NetPrefixLengthInvalid,'hm2VlanIdNotExists':hm2VlanIdNotExists,'hm2NetIPv6AddressAlreadyExists':hm2NetIPv6AddressAlreadyExists,'hm2NetIPv6ChangeEUIWhileEntryActive':hm2NetIPv6ChangeEUIWhileEntryActive,'hm2NetIPv6ChangeAddressWhileEntryActive':hm2NetIPv6ChangeAddressWhileEntryActive,'hm2NetIPv6IncorrectFamilyType':hm2NetIPv6IncorrectFamilyType,'hm2NetIPv6EnableEUIWhilePrefixLenNot64':hm2NetIPv6EnableEUIWhilePrefixLenNot64,'hm2NetIPv6ChangeAddressOrigin':hm2NetIPv6ChangeAddressOrigin,'hm2NetIPv6MaximumNumberStaticAddresses':hm2NetIPv6MaximumNumberStaticAddresses,'hm2NetIPv6IncorrectAddressLength':hm2NetIPv6IncorrectAddressLength,'hm2NetIPv6AddressPrefixNotMatching':hm2NetIPv6AddressPrefixNotMatching,'hm2NetIPv6PrefixNotSupported':hm2NetIPv6PrefixNotSupported,'hm2NetIPv6CannotAddReservedAddress':hm2NetIPv6CannotAddReservedAddress,'hm2EntryLenCharset':hm2EntryLenCharset,'hm2UserPwdLen':hm2UserPwdLen,'hm2EntryNotExist':hm2EntryNotExist,'hm2MaxNumUserExceeded':hm2MaxNumUserExceeded,'hm2NetIPv6UnreachableGatewaySubnet':hm2NetIPv6UnreachableGatewaySubnet,'hm2GenericDeleteError':hm2GenericDeleteError,'hm2GenericCreateError':hm2GenericCreateError,'hm2GenericEntryNotExist':hm2GenericEntryNotExist,'hm2GenericIPv4IPv6Supported':hm2GenericIPv4IPv6Supported,'hm2GenericMulticastAddrNotAllowed':hm2GenericMulticastAddrNotAllowed,'hm2GenericIPAddrInvalid':hm2GenericIPAddrInvalid,'hm2GenericSourcePortInvalid':hm2GenericSourcePortInvalid,'hm2GenericRowCommitError':hm2GenericRowCommitError,'hm2GenericDestIPAddrInvalid':hm2GenericDestIPAddrInvalid,'hm2GenericDestMACAddrInvalid':hm2GenericDestMACAddrInvalid,'hm2GenericDestPortInvalid':hm2GenericDestPortInvalid,'hm2GenericSourceIPAddrInvalid':hm2GenericSourceIPAddrInvalid,'hm2GenericSourceMACAddrInvalid':hm2GenericSourceMACAddrInvalid,'hm2GenericEntryInvalid':hm2GenericEntryInvalid,'hm2GenericInterfaceInvalid':hm2GenericInterfaceInvalid,'hm2GenericOnlySupportsIPv4':hm2GenericOnlySupportsIPv4,'hm2GenericVlanIdInvalid':hm2GenericVlanIdInvalid,'hm2GenericCommitInProgress':hm2GenericCommitInProgress,'hm2GenericNameInvalid':hm2GenericNameInvalid,'hm2GenericDirectionInvalid':hm2GenericDirectionInvalid,'hm2GenericNameAlreadyExist':hm2GenericNameAlreadyExist,'hm2GenericMinEntryInvalid':hm2GenericMinEntryInvalid,'hm2GenericEntryExistInSharedTable':hm2GenericEntryExistInSharedTable,'hm2GenericEntryIsReadOnly':hm2GenericEntryIsReadOnly,'hmMgmtSEInfoIDGroup':hmMgmtSEInfoIDGroup,'hmMgmtSEInfoValueChanged':hmMgmtSEInfoValueChanged})